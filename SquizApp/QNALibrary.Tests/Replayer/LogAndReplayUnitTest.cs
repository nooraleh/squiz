using FluentAssertions;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace QNALibrary.Tests.Replayer
{
    public class LogAndReplayUnitTest
    {
        public static void SimulateFailedQNA()
        {
            int nFails = SquizManager.Instance.QNASubmapping.Count;
            for (int i = 0; i < nFails; ++i)
            {
                SquizManager.Instance.CurrentQNAFail();
            }
        }


        [Theory]
        [InlineData(50, 73, "Gregoire")]
        public void SquizManager_Logs_QNACollection_RoundTrips(int startRange, int endRange, string selectedDropdown)
        {
            /*
             Testing summary:
                - Generate a series of QNA (manual mode so deterministic)
                - fail them all
                - log the failed QNA to .json file
                - reload them from the .json
                - confirm equivalence of initial QNA data structure with that of data structure
                  loaded from .json
             */

            SquizManager.Instance.ManualSetup(startRange, endRange, selectedDropdown, new QNACollection());

            Queue<Dictionary<string, string>> expectedQNAMapping = SquizManager.Instance.QNASubmapping;

            LogAndReplayUnitTest.SimulateFailedQNA();

            string fullPathToLogFile = SquizManager.Instance.LogFailedQNA();

            Queue<Dictionary<string, string>> resultQNAMapping = SquizManager.Instance.LoadFailedQNA(fullPathToLogFile);

            expectedQNAMapping.Should().BeEquivalentTo(resultQNAMapping);
        }


        [Theory]
        [InlineData(0, 3, "TestLatexSnippetLogic")]
        [InlineData(0, 1, "TestImageDisplay")]
        public void SquizManager_Logs_QNATestCollection_NoLogs(int startRange, int endRange, string selectedDropdown)
        {
            /*
             Unit tests confirming that component QNA of `QNATestCollection` do not log failed QNA (or at all).
             */

            SquizManager.Instance.ManualSetup(startRange, endRange, selectedDropdown, new QNATestCollection());

            LogAndReplayUnitTest.SimulateFailedQNA();

            string fullPathToLogFile = SquizManager.Instance.LogFailedQNA();

            // `fullPathToLogFile` as there should be no log file, hence no logging
            fullPathToLogFile.Should().BeEmpty();
        }
    }
}
