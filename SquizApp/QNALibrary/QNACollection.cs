using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Reflection.Metadata.Ecma335;
using System.Text;
using System.Threading.Tasks;

namespace QNALibrary;

using QNACollectionMapping = Dictionary<string, QNABase>;

public class QNACollection
{
    public static QNACollectionMapping qnaCollectionMapping = new();
    public QNACollection()
    {
        Add(new Gregoire.Gregoire());
        Add(new mappings.Test.TestLatexSnippetLogic());
    }

    private void Add(QNABase qnaBase)
    {
        qnaCollectionMapping.Add(qnaBase.ToString(), qnaBase);
    }

    public Dictionary<int, Dictionary<string, string>> qnaMapping(string qnaKey)
    {
        return qnaCollectionMapping[qnaKey].QNAMapping;
    }

    public QNACategory qnaCategory(string qnaKey)
    {
        return qnaCollectionMapping[qnaKey].Category;
    }

    //public Dictionary<int,Dictionary<string, string>> GetRandomSubcollection(int nQNA, string qnaKey)
    //{
    //    Dictionary<int, Dictionary<string, string>> localQNAMapping = qnaMapping(qnaKey);

    //    // Validate the input size
    //    if (nQNA < 1)
    //    {
    //        throw new ArgumentException("Size must be at least 1.");
    //    }

    //    if (nQNA > localQNAMapping.Count)
    //    {
    //        throw new ArgumentException($"Size must not exceed the size of the collection. Collection size: {localQNAMapping.Count}");
    //    }

    //    // Get a randomized subcollection of the specified size
    //    var random = new Random();
    //    return localQNAMapping
    //        .OrderBy(x => random.Next())
    //        .Take(nQNA)
    //        .ToDictionary(pair => pair.Key, pair => pair.Value);
    //}


    public Queue<Dictionary<string, string>> GetRandomSubcollection(int nQNA, string qnaKey)
    {
        Dictionary<int, Dictionary<string, string>> localQNAMapping = qnaMapping(qnaKey);

        // Validate the input size
        if (nQNA < 1)
        {
            throw new ArgumentException("Size must be at least 1.");
        }

        if (nQNA > localQNAMapping.Count)
        {
            throw new ArgumentException($"Size must not exceed the size of the collection. Collection size: {localQNAMapping.Count}");
        }

        // Get a randomized subcollection of the specified size
        var random = new Random();
        var randomSubcollection = localQNAMapping
            .OrderBy(x => random.Next())
            .Take(nQNA)
            .Select(pair => pair.Value)
            .ToList();

        // Add an index to each qna
        string qnaIndex = "0";
        foreach (var qna in randomSubcollection)
        {
            qna.Add("index", $"{Int32.Parse(qnaIndex) + 1}");
        }


        // Create a Queue from the selected subcollection
        return new Queue<Dictionary<string, string>>((IEnumerable<Dictionary<string, string>>)randomSubcollection);
    }

    public QNACategory GetQNACategory(string qnaKey)
    {
        return qnaCategory(qnaKey);
    }

}
