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
        [InlineData(12, 45, "CBasics")]
        [InlineData(24, 34, "BoostAsio")]
        [InlineData(19, 37, "CiscoAdvancedCPP")]
        [InlineData(19, 37, "CPPBasics")]
        [InlineData(2, 45, "CPPConcurrency")]
        [InlineData(45, 74, "CPPYouTube")]
        [InlineData(3, 7, "DesignPatternsCPP20")]
        [InlineData(37, 65, "EffectiveCPP11_14")]
        [InlineData(50, 73, "Gregoire")]
        [InlineData(5, 24, "CPPSTL")]
        [InlineData(45, 82, "CS11DotNet7")]
        [InlineData(13, 27, "CSharpIntermediate")]
        [InlineData(1, 21, "DotNetMaui")]
        [InlineData(29, 54, "KeyFinancialMarketsConcepts")]
        [InlineData(32, 96, "OptionsFuturesOtherDerivatives")]
        [InlineData(4, 39, "PracticalCPP20Finance")]
        [InlineData(43, 45, "NetworkProgramming")]
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
