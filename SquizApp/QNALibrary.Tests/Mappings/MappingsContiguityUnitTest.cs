using FluentAssertions;
using QNALibrary.mappings.C;


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


    }
}
