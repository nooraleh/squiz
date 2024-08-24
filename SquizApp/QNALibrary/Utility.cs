using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;

namespace QNALibrary
{
    public class Utility
    {
        public static string GenerateLatexDocument(QNACategory qnaCategory, string codeSnippet)
        {
            string latexTemplate;
            switch (qnaCategory)
            {
                case QNACategory.CPP:
                    latexTemplate = @"
\documentclass{article}
\usepackage{minted}

\begin{document}

\section*{Example C++ Function}

Here is a simple C++ function:

\begin{minted}[linenos, breaklines, frame=single]{cpp}
{0}
\end{minted}

\end{document}
";
                    break;
                case QNACategory.CSharp:
                    latexTemplate = @"
\documentclass{article}
\usepackage{minted}

\begin{document}

\section*{Example C# Function}

Here is a simple C# function:

\begin{minted}[linenos, breaklines, frame=single]{csharp}
{0}
\end{minted}

\end{document}
";
                    break;
                default:
                    latexTemplate = @"
\documentclass{article}

\begin{document}

\section*{Snippet}

Snippet:
${0}$
\end{document}
";
                    break;

            }

            return string.Format(latexTemplate, codeSnippet);
        }


    }
}
