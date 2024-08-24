using System;
using System.Collections.Generic;
using System.Diagnostics;
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

        public static string CompileLatexDocumentToPDF(string textFilePath, string latexDocument)
        {
            // textFilePath will be based on the QNA in question

            return string.Empty;
        }

        public static void DisplayLatexPDF(string texFilePath, string latexCode)
        {
            // to be called in the 'displaySnippetButton_OnClick' event handler
            File.WriteAllText(texFilePath, latexCode);

            // Compile the .tex file to a PDF using pdflatex with -shell-escape option
            ProcessStartInfo psi = new ProcessStartInfo();
            psi.FileName = "pdflatex";
            psi.Arguments = $"-shell-escape -interaction=nonstopmode {texFilePath}";
            psi.RedirectStandardOutput = true;
            psi.RedirectStandardError = true;
            psi.UseShellExecute = false;

            Process process = Process.Start(psi);
            process.WaitForExit();
        }

        public static void DisplayLatexPDF(string texFilePath)
        {
            // Display the generated PDF (using default PDF viewer)
            string pdfFilePath = Path.ChangeExtension(texFilePath, ".pdf");
            if (File.Exists(pdfFilePath))
            {
                Process.Start(new ProcessStartInfo(pdfFilePath) { UseShellExecute = true });
            }
            else
            {
                Console.WriteLine("PDF generation failed.");
            }
        }

    }
}
