namespace QNALibrary;

public class QNABase
{
    public string Title { get; set; }

    public QNACategory Category { get; set; }

    public Dictionary<int, Dictionary<string, string>> qnaMapping { get; set; }

    public List<Dictionary<string, string>> BuildRandomMode(int qnaSize = 10)
    {
        List<int> keyList = new(qnaMapping.Keys);
        Random randomizer = new();

        List<Dictionary<string, string>> returnList = new();

        for (int i = 0; i < qnaSize; ++i)
        {
            returnList.Add( qnaMapping[randomizer.Next(keyList.Count)]);
        }

        return returnList;
    }
}
