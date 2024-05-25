using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
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

        public Queue<Dictionary<string, string>> QNASubmapping { get; set; }

        public Dictionary<string, string> CurrentQNA { get; set; }

        public void CurrentQNAPass()
        {
            // TODO: Implement (calls .Next() to move the CurrentQNA along)

            NextQNA(true);
        }

        public void Setup(int nQNA, string qnaKey)
        {
            QNACollection qnaCollection = new();
            NQuestions = nQNA;
            QNASubmapping = qnaCollection.GetRandomSubcollection(nQNA, qnaKey);
            CurrentQNA = QNASubmapping.Dequeue();
        }

        public void AddUserAnswer(string userAnswer)
        {
            // if we can't add it then it already exists
            if (!CurrentQNA.TryAdd("userA", userAnswer))
            {
                CurrentQNA["userA"] = userAnswer;
            }
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

        public string ModelAnswer()
        {
            return CurrentQNA["a"];
        }

        public string Question()
        {
            return CurrentQNA["q"];
        }


        public void CurrentQNAFail()
        {
            // TODO: Implement (calls .Next() to move the CurrentQNA along)

            NextQNA(false);
        }

        private void NextQNA(bool pass)
        {
            // pops the currentQNA to the back of the list if false, removes if true
            if (pass)
            {
                CurrentQNA = QNASubmapping.Dequeue();
            }
            else
            {
                QNASubmapping.Enqueue(CurrentQNA);
                CurrentQNA = QNASubmapping.Dequeue();
            }
        }

    }
}
