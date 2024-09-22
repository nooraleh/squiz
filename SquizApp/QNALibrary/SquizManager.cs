﻿using QNALibrary.mappings.CPP;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

namespace QNALibrary
{
    public sealed class SquizManager
    {
        private static Lazy<SquizManager> squizManagerInstance = new Lazy<SquizManager>(() => new SquizManager());

        private SquizManager()
        {
        }

        public int NumberOfQuestions;

        // provide global access to the instance
        public static SquizManager Instance
        {
            get
            {
                return squizManagerInstance.Value;
            }
        }

        public int NQuestions { get; set;}

        private bool ShouldLogFailedQNA { get; set; }

        public Queue<Dictionary<string, string>> QNASubmapping { get; set; }

        public Queue<Dictionary<string, string>> FailedQNAMappingQueue { get; set; }

        public Dictionary<string, string> CurrentQNA { get; set; }

        public void CurrentQNAPass()
        {
            NextQNA(true);
        }

        public void RandomSetup(int nQNA, string qnaKey, QNACollection qnaCollection)
        {
            NQuestions = nQNA;
            QNASubmapping = qnaCollection.GetRandomSubcollection(nQNA, qnaKey);
            FailedQNAMappingQueue = new();
            Title = qnaKey;
            Category = qnaCollection.GetQNACategory(qnaKey);

            // assign first QNA to `CurrentQNA`
            NextQNA();

            // compile relevant snippets into LaTeX pdf files
            CompileSubmappingSnippetsLaTeX( QNASubmapping);

            // QNATestCollection component classes should not be logged
            ShouldLogFailedQNA = qnaCollection.ShouldLogFailedQNA;
        }

        public void ManualSetup(int startRange, int endRange, string qnaKey, QNACollection qnaCollection)
        {
            QNASubmapping = qnaCollection.GetManualSubcollection(startRange, endRange, qnaKey);
            FailedQNAMappingQueue = new();
            Title = qnaKey;
            Category = qnaCollection.GetQNACategory(qnaKey);

            // assign first QNA to `CurrentQNA`
            NextQNA();

            // compile relevant snippets into LaTeX pdf files
            CompileSubmappingSnippetsLaTeX(QNASubmapping);

            // QNATestCollection component classes should not be logged
            ShouldLogFailedQNA = qnaCollection.ShouldLogFailedQNA;
        }

        public void ReplayerSetup(string fullPathToLogFile)
        {
            QNASubmapping = LoadFailedQNA(fullPathToLogFile);
            FailedQNAMappingQueue = new();

            QNACollection qnaCollection = new();

            // since the formatting of the filename is $"{Title}-{DateTime.Now.ToString("yyyyMMdd-HHmm")}.json"
            string qnaKey = Path.GetFileName(fullPathToLogFile).Split('-')[0];
            Title = qnaKey;
            Category = qnaCollection.GetQNACategory(qnaKey);

            // assign first QNA to `CurrentQNA`
            NextQNA();

            // compile relevant snippets into LaTeX pdf files
            CompileSubmappingSnippetsLaTeX(QNASubmapping);

            // QNATestCollection component classes should not be logged
            ShouldLogFailedQNA = qnaCollection.ShouldLogFailedQNA;
        }


        public void CompileSubmappingSnippetsLaTeX(Queue<Dictionary<string, string>> qnaSubMapping)
        {
            // compiles any snippetA/snippetQ value strings into LaTeX based pdfs
            // will be part of the SQUIZ loading phase

            // compile the first QNA in the queue
            CompileQNA(CurrentQNA);

            foreach (var queueItem in qnaSubMapping)
            {
                CompileQNA(queueItem);
            }
        }

        private void CompileQNA(Dictionary<string, string> qnaItem)
        {
            if (qnaItem["snippetA"] != string.Empty)
            {
                string texFileName = $@"{Title}-{qnaItem["ID"]}-{qnaItem["index"]}-snippetA.tex";
                Utility.GenerateAndCompileLatexDocumentToPDF(texFileName, qnaItem["snippetA"], Category);
            }
            else if (qnaItem["snippetQ"] != string.Empty)
            {
                string texFileName = $"{Title}-{qnaItem["ID"]}-{qnaItem["index"]}-snippetQ.tex";
                Utility.GenerateAndCompileLatexDocumentToPDF(texFileName, qnaItem["snippetQ"], Category);
            }
        }


        public string Title { get; set; }

        public QNACategory Category { get; set; }

        public void AddUserAnswer(string userAnswer)
        {
            // if we can't add it then it already exists
            if (!CurrentQNA.TryAdd("userA", userAnswer))
            {
                CurrentQNA["userA"] = userAnswer;
            }
        }

        public string Index()
        {
            return CurrentQNA["index"];
        }

        public string ID()
        {
            return CurrentQNA["ID"];
        }


        public string UserAnswer()
        {
            string tryValue = string.Empty;
            if (CurrentQNA.TryGetValue("userA", out tryValue))
            {
                return tryValue;
            }
            else
            {
                return "User answer unavailable";
            }
        }

        public string SnippetA()
        {
            string tryValue;
            if (CurrentQNA.TryGetValue("snippetA", out tryValue))
            {
                return tryValue;
            }
            else
            {
                return string.Empty;
            }
        }

        public string SnippetQ()
        {
            string tryValue;
            if (CurrentQNA.TryGetValue("snippetQ", out tryValue))
            {
                return tryValue;
            }
            else
            {
                return string.Empty;
            }
        }

        public string ImageQ()
        {
            string tryValue;
            if (CurrentQNA.TryGetValue("imgQ", out tryValue))
            {
                string[] path = new string[] { AppContext.BaseDirectory, "Images", Title, tryValue };
                return Path.Combine(path);
            }
            else
            {
                return string.Empty;
            }
        }

        public string ImageA()
        {
            string tryValue;
            if (CurrentQNA.TryGetValue("imgA", out tryValue))
            {
                string[] path = new string[] { AppContext.BaseDirectory , "Images", Title, tryValue };
                return Path.Combine(path);
            }
            else
            {
                return string.Empty;
            }
        }
        public bool ImageQExists()
        {
            string tryValue;
            if (CurrentQNA.TryGetValue("imgQ", out tryValue))
            {
                string[] path = new string[] { AppContext.BaseDirectory, "Images", Title, tryValue };
                return File.Exists(Path.Combine(path));
            }
            else
            {
                return false;
            }
        }

        public bool ImageAExists()
        {
            string tryValue;
            if (CurrentQNA.TryGetValue("imgA", out tryValue))
            {
                string[] path = new string[] { AppContext.BaseDirectory, "Images", Title, tryValue };
                return File.Exists(Path.Combine(path));
            }
            else
            {
                return false;
            }
        }

        public string ModelAnswer()
        {
            return CurrentQNA["a"];
        }

        public string Question()
        {
            return CurrentQNA["q"];
        }

        public string NAttempts()
        {
            // number of attempts at the current question
            return CurrentQNA["nAttempts"];
        }

        public void CurrentQNAFail()
        {
            EnqueueFailedQNAMappingQueue();

            NextQNA(false);
        }

        private void EnqueueFailedQNAMappingQueue()
        {
            // don't want to log duplicate QNA - since we already have 
            // a mechanism for repeating failed qna intra-squiz
            if (!FailedQNAMappingQueue.Contains(CurrentQNA))
            {
                FailedQNAMappingQueue.Enqueue(CurrentQNA);
            }
        }


        private void NextQNA(bool pass)
        {
            // pops the currentQNA to the back of the list if false, removes if true
            if (pass)
            {
                QNASubmapping.Dequeue();
                NextQNA();
            }
            else
            {
                QNASubmapping.Enqueue(CurrentQNA);
                QNASubmapping.Dequeue();
                NextQNA();
            }
        }

        public void LogFailedQNA()
        {
            if (ShouldLogFailedQNA)
            {
                string logFileName = $"{Title}-{DateTime.Now.ToString("yyyyMMdd-HHmm")}.json";
                string logFilePath = Path.Combine(Utility.LogsDirectory(), logFileName);

                string failedQNAJSON = JsonSerializer.Serialize(FailedQNAMappingQueue);

                File.WriteAllText(logFilePath, failedQNAJSON);
            }
        }

        public Queue<Dictionary<string, string>> LoadFailedQNA(string fullPathToLogFile)
        {
            string jsonQNA = File.ReadAllText(fullPathToLogFile);
            return JsonSerializer.Deserialize<Queue<Dictionary<string, string>>>(jsonQNA);
        }

        private void NextQNA()
        {
            if (!IsEmpty())
            {
                CurrentQNA = QNASubmapping.Peek();
            }

            string nAttemptsTryValue = "0";
            if (!CurrentQNA.TryAdd("nAttempts", nAttemptsTryValue))
            {
                CurrentQNA["nAttempts"] = $"{Int32.Parse(CurrentQNA["nAttempts"]) + 1}";
            }
        }

        public bool IsEmpty()
        {
            return SquizManager.Instance.QNASubmapping.Count == 0;
        }

    }
}
