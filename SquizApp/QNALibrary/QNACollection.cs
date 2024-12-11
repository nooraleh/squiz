namespace QNALibrary;

using static System.Runtime.InteropServices.JavaScript.JSType;
using QNACollectionMapping = Dictionary<string, QNABase>;

public class QNACollection
{
    public static QNACollectionMapping qnaCollectionMapping = new();
    public QNACollection()
    {
        PopuplateQNACollectionMapping();
    }

    protected virtual void PopuplateQNACollectionMapping()
    {
        Add(new QNALibrary.mappings.C.CBasics());
        Add(new QNALibrary.mappings.CPP.BoostAsio());
        Add(new QNALibrary.mappings.CPP.CiscoAdvancedCPP());
        Add(new QNALibrary.mappings.CPP.CPPBasics());
        Add(new QNALibrary.mappings.CPP.CPPConcurrency());
        Add(new QNALibrary.mappings.CPP.CPPYouTube());
        Add(new QNALibrary.mappings.CPP.DesignPatternsCPP20());
        Add(new QNALibrary.mappings.CPP.EffectiveCPP11_14());
        Add(new QNALibrary.mappings.CPP.Gregoire());
        Add(new QNALibrary.mappings.CPP.CPPSTL());
        Add(new QNALibrary.mappings.CPP.ExpertCpp());
        Add(new QNALibrary.mappings.CPP.ModernCMake());
        Add(new QNALibrary.mappings.CPP.CPP20CompleteGuide());
        Add(new QNALibrary.mappings.CSharp.CS11DotNet7());
        Add(new QNALibrary.mappings.CSharp.CSharpIntermediate());
        Add(new QNALibrary.mappings.CSharp.DotNetMaui());
        Add(new QNALibrary.mappings.Finance.KeyFinancialMarketsConcepts());
        Add(new QNALibrary.mappings.Finance.OptionsFuturesOtherDerivatives());
        Add(new QNALibrary.mappings.Finance.PracticalCPP20Finance());
        Add(new QNALibrary.mappings.Software.NetworkProgramming());
        Add(new QNALibrary.mappings.Software.DevelopersGuideToLinux());
    }

    // tells the SquizManager whether the QNABase objects in the collection
    // should log failed QNA
    public virtual bool ShouldLogFailedQNA { get; } = true;

    protected void Add(QNABase qnaBase)
    {
        qnaCollectionMapping.TryAdd(qnaBase.ToString(), qnaBase);
    }

    public Dictionary<int, Dictionary<string, string>> qnaMapping(string qnaKey)
    {
        return qnaCollectionMapping[qnaKey].QNAMapping;
    }

    public QNACategory qnaCategory(string qnaKey)
    {
        return qnaCollectionMapping[qnaKey].Category;
    }

    public Queue<Dictionary<string, string>> GetManualSubcollection(int startRange, int endRange, string qnaKey)
    {
        Dictionary<int, Dictionary<string, string>> localQNAMapping = qnaMapping(qnaKey);

        Dictionary<int, Dictionary<string, string>> subsetCandidate = new Dictionary<int, Dictionary<string, string>>();
        
        for (int i = startRange; i <= endRange; i++)
        {
            if (localQNAMapping.ContainsKey(i))
            {
                subsetCandidate[i] = localQNAMapping[i]; // add to the subset
            }
        }

        // use this type so we can finish with the same logic as `GetRandomSubcollection`
        var subsetCandidateList = subsetCandidate.ToList();

        // Add an index and ID to each qna
        string qnaIndex = "0";
        foreach (var kvp in subsetCandidateList)
        {
            // Access the original dictionary (Value) and the ID (Key)
            var qna = kvp.Value;
            qnaIndex = $"{Int32.Parse(qnaIndex) + 1}";

            // Add "index" and "ID" to the dictionary
            qna.Add("index", qnaIndex);
            qna.Add("ID", kvp.Key.ToString());
        }

        return new Queue<Dictionary<string, string>>(subsetCandidateList.Select(kvp => kvp.Value));
    }


    public Queue<Dictionary<string, string>> GetRandomSubcollection(int nQNA, string qnaKey)
    {
        Dictionary<int, Dictionary<string, string>> localQNAMapping = qnaMapping(qnaKey);

        // Validate the input size
        if (nQNA < 1)
        {
            // TODO: Don't really like the idea of throwing an exception - bit too agressive for user
            // input - perhaps a MessageBox up the call stack where System.Windows.Forms.MessageBox is available
            // UPDATE: Perhaps control the maxsize via the control (ManualModeForm already has something similar)
            throw new ArgumentException("Size must be at least 1.");
        }

        if (nQNA > localQNAMapping.Count)
        {
            // TODO: Don't really like the idea of throwing an exception - bit too agressive for user
            // input - perhaps a MessageBox up the call stack where System.Windows.Forms.MessageBox is available
            throw new ArgumentException($"Size must not exceed the size of the collection. Collection size: {localQNAMapping.Count}");
        }

        // get a randomized subcollection of the specified size
        var random = new Random();
        var randomSubcollection = localQNAMapping
            .OrderBy(x => random.Next())
            .Take(nQNA)
            .ToList();

        // add an index and ID to each qna
        string qnaIndex = "0";
        foreach (var kvp in randomSubcollection)
        {
            // access the original dictionary (Value) and the ID (Key)
            var qna = kvp.Value;
            qnaIndex = $"{Int32.Parse(qnaIndex) + 1}";

            // add "index" and "ID" to the dictionary
            qna.Add("index", qnaIndex);
            qna.Add("ID", kvp.Key.ToString());
        }

        return new Queue<Dictionary<string, string>>(randomSubcollection.Select(kvp => kvp.Value));
    }

    public QNACategory GetQNACategory(string qnaKey)
    {
        return qnaCategory(qnaKey);
    }

}
