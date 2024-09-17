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

}
