using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Reflection;
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
                case QNACategory.C:
                case QNACategory.CPP:
                    latexTemplate = @"
\documentclass{{article}}
\usepackage{{minted}}

\begin{{document}}

\section*{{C++ Snippet}}


\begin{{minted}}[linenos, breaklines, frame=single]{{cpp}}
{0}
\end{{minted}}

\end{{document}}
";
                    break;
                case QNACategory.CSharp:
                    latexTemplate = @"
\documentclass{{article}}
\usepackage{{minted}}

\begin{{document}}

\section*{{C# Snippet}}


\begin{{minted}}[linenos, breaklines, frame=single]{{csharp}}
{0}
\end{{minted}}

\end{{document}}
";
                    break;
                default:
                    latexTemplate = @"
\documentclass{{article}}

\begin{{document}}

\section*{{Snippet}}

Snippet:
${0}$
\end{{document}}
";
                    break;

            }

            return string.Format(latexTemplate, codeSnippet);
        }

        public static string GenerateAndCompileLatexDocumentToPDF(string texFilePath, string codeSnippet, QNACategory qnaCategory)
        {
            string generatedLatex = GenerateLatexDocument(qnaCategory, codeSnippet);
            CompileLatexPDF(FullTextFilePath(texFilePath), generatedLatex);

            return string.Empty;
        }

        public static string FullTextFilePath(string texFileName)
        {
            return Path.Combine(SnippetsDirectory(), texFileName);
        }


        public static string SnippetsDirectory()
        {
            string appDirectory = AppContext.BaseDirectory;
            string snippetSubDirectory = "Snippets";
            string fullSnippetsPath = Path.Combine(appDirectory, snippetSubDirectory);

            // create the directory if it does not exist
            Directory.CreateDirectory(fullSnippetsPath);
            return fullSnippetsPath;
        }


        public static void CompileLatexPDF(string texFilePath, string latexCode)
        {
            File.WriteAllText(texFilePath, latexCode);

            // compile the .tex file to a PDF using pdflatex with -shell-escape option
            ProcessStartInfo psi = new ProcessStartInfo();
            psi.FileName = "pdflatex";
            psi.Arguments = $"-shell-escape -interaction=nonstopmode {texFilePath}";
            psi.WorkingDirectory = Path.GetDirectoryName(texFilePath);
            psi.RedirectStandardOutput = true;
            psi.RedirectStandardError = true;
            psi.UseShellExecute = false;

            // prevent command prompt window from appearing
            psi.CreateNoWindow = true;

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
                // "PDF generation failed"
            }
        }

        public static bool IsDebugMode()
        {
            bool isDebug = false;
#if DEBUG
            isDebug = true;
#endif
            return isDebug;
        }

        public static string LogsDirectory()
        {
            string logsDirectory = Path.Combine(
            Environment.GetFolderPath(
                Environment.SpecialFolder.LocalApplicationData),
                Assembly.GetEntryAssembly().GetName().Name,
                "Logs"
            );

            // ensure directory exists
            Directory.CreateDirectory(logsDirectory);

            return logsDirectory;
        }

    }
}
