using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace QNALibrary;

public class QNATestCollection : QNACollection
{
    public QNATestCollection()
    {
        PopuplateQNACollectionMapping();
    }

    protected override void PopuplateQNACollectionMapping()
    {
        qnaCollectionMapping.Clear();
        Add(new mappings.Test.TestLatexSnippetLogic());
    }


}
