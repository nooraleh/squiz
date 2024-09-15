namespace QNALibrary;
using QNAMappingType = Dictionary<int, Dictionary<string, string>>;

public class QNABase
{
    public QNABase(string title, QNACategory category, QNAMappingType qnaMapping)
    {
        Title = title;
        Category = category;
        QNAMapping = qnaMapping;
    }

    public string Title { get; set; }

    public QNACategory Category { get; set; }

    public QNAMappingType QNAMapping { get; set; }

    public int Count { get { return QNAMapping.Count; } }

    public List<Dictionary<string, string>> BuildRandomMode(int qnaSize = 10)
    {
        List<int> keyList = new(QNAMapping.Keys);
        Random randomizer = new();

        List<Dictionary<string, string>> returnList = new();

        for (int i = 0; i < qnaSize; ++i)
        {
            returnList.Add(QNAMapping[randomizer.Next(keyList.Count)]);
        }

        return returnList;
    }
}
