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

    public override bool ShouldLogFailedQNA { get; } = false;

    protected override void PopuplateQNACollectionMapping()
    {
        qnaCollectionMapping.Clear();
        Add(new mappings.Test.TestLatexSnippetLogic());
        Add(new mappings.Test.TestImageDisplay());
    }


}
