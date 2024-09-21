using FluentAssertions;
using QNALibrary.mappings.C;
using QNALibrary.mappings.CPP;
using QNALibrary.mappings.CSharp;
using QNALibrary.mappings.Finance;
using QNALibrary.mappings.Software;
using QNALibrary.mappings.Template;


namespace QNALibrary.Tests.Mappings
{
    public class MappingsContiguityUnitTest
    {
        public static IEnumerable<int> GetMissingKeys(QNABase qnaBase)
        {
            List<int> missingKeys = new List<int>();

            int minKey = 1;
            int maxKey = qnaBase.QNAMapping.Keys.Count > 0 ? qnaBase.QNAMapping.Keys.Max() : 0;

            // loop from minKey to maxKey and check for gaps
            for (int i = minKey; i <= maxKey; i++)
            {
                if (!qnaBase.QNAMapping.ContainsKey(i))
                {
                    missingKeys.Add(i);
                }
            }

            return missingKeys;
        }

        [Fact]
        public void QNALibrary_mappings_C_CBasics()
        {
            var result = MappingsContiguityUnitTest.GetMissingKeys(new CBasics());
            result.Should().BeEmpty();
        }

        [Fact]
        public void QNALibrary_mappings_CPP_BoostAsio()
        {
            var result = MappingsContiguityUnitTest.GetMissingKeys(new BoostAsio());
            result.Should().BeEmpty();
        }
 
        [Fact]
        public void QNALibrary_mappings_CPP_CiscoAdvancedCP()
        {
            var result = MappingsContiguityUnitTest.GetMissingKeys(new CiscoAdvancedCPP());
            result.Should().BeEmpty();
        }

        [Fact]
        public void QNALibrary_mappings_CPP_CPPBasics()
        {
            var result = MappingsContiguityUnitTest.GetMissingKeys(new CPPBasics());
            result.Should().BeEmpty();
        }

        [Fact]
        public void QNALibrary_mappings_CPP_CPPConcurrency()
        {
            var result = MappingsContiguityUnitTest.GetMissingKeys(new CPPConcurrency());
            result.Should().BeEmpty();
        }

        [Fact]
        public void QNALibrary_mappings_CPP_CPPSTL()
        {
            var result = MappingsContiguityUnitTest.GetMissingKeys(new CPPSTL());
            result.Should().BeEmpty();
        }

        [Fact]
        public void QNALibrary_mappings_CPP_CPPYouTube()
        {
            var result = MappingsContiguityUnitTest.GetMissingKeys(new CPPYouTube());
            result.Should().BeEmpty();
        }

        [Fact]
        public void QNALibrary_mappings_CPP_DesignPatternsCPP20()
        {
            var result = MappingsContiguityUnitTest.GetMissingKeys(new DesignPatternsCPP20());
            result.Should().BeEmpty();
        }

        [Fact]
        public void QNALibrary_mappings_CPP_EffectiveCPP11_14()
        {
            var result = MappingsContiguityUnitTest.GetMissingKeys(new EffectiveCPP11_14());
            result.Should().BeEmpty();
        }

        [Fact]
        public void QNALibrary_mappings_CPP_Gregoire()
        {
            var result = MappingsContiguityUnitTest.GetMissingKeys(new Gregoire());
            result.Should().BeEmpty();
        }

        [Fact]
        public void QNALibrary_mappings_CSharp_CS11DotNet7()
        {
            var result = MappingsContiguityUnitTest.GetMissingKeys(new CS11DotNet7());
            result.Should().BeEmpty();
        }

        [Fact]
        public void QNALibrary_mappings_CSharp_CSharpIntermediate()
        {
            var result = MappingsContiguityUnitTest.GetMissingKeys(new CSharpIntermediate());
            result.Should().BeEmpty();
        }

        [Fact]
        public void QNALibrary_mappings_CSharp_DotNetMaui()
        {
            var result = MappingsContiguityUnitTest.GetMissingKeys(new DotNetMaui());
            result.Should().BeEmpty();
        }

        [Fact]
        public void QNALibrary_mappings_Finance_KeyFinancialMarketsConcepts()
        {
            var result = MappingsContiguityUnitTest.GetMissingKeys(new KeyFinancialMarketsConcepts());
            result.Should().BeEmpty();
        }

        [Fact]
        public void QNALibrary_mappings_Finance_OptionsFuturesOtherDerivatives()
        {
            var result = MappingsContiguityUnitTest.GetMissingKeys(new OptionsFuturesOtherDerivatives());
            result.Should().BeEmpty();
        }

        [Fact]
        public void QNALibrary_mappings_Finance_PracticalCPP20Finance()
        {
            var result = MappingsContiguityUnitTest.GetMissingKeys(new PracticalCPP20Finance());
            result.Should().BeEmpty();
        }

        [Fact]
        public void QNALibrary_mappings_Software_NetworkProgramming()
        {
            var result = MappingsContiguityUnitTest.GetMissingKeys(new NetworkProgramming());
            result.Should().BeEmpty();
        }

        [Fact]
        public void QNALibrary_mappings_Template_Template()
        {
            var result = MappingsContiguityUnitTest.GetMissingKeys(new Template());
            result.Should().BeEmpty();
        }
    }
}
