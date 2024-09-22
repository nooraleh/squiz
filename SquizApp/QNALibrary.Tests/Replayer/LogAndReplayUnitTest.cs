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


        [Fact]
        public void SquizManager_Logs_RoundTrips_Gregory() // TODO: Could be a thoery with inline data being the ManualSetup arguments
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

            (int startRange, int endRange, string selectedDropdown, QNACollection qnaCollection) = (50, 73, "Gregoire", new QNACollection());

            SquizManager.Instance.ManualSetup(startRange, endRange, selectedDropdown, qnaCollection);

            Queue<Dictionary<string, string>> expectedQNAMapping = SquizManager.Instance.QNASubmapping;

            LogAndReplayUnitTest.SimulateFailedQNA();

            string fullPathToLogFile = SquizManager.Instance.LogFailedQNA();

            Queue<Dictionary<string, string>> resultQNAMapping = SquizManager.Instance.LoadFailedQNA(fullPathToLogFile);


            expectedQNAMapping.Should().BeEquivalentTo(resultQNAMapping);
        }

    }
}
