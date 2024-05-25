using QNALibrary;

namespace SquizApp
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }

        private void startQuizButton_Click(object sender, EventArgs e)
        {
            //qnaDropdownComboBox.Text
            //QNACollection qnaCollection = new();

            //Dictionary<int, Dictionary<string, string>> liveQNA = qnaCollection.GetRandomSubcollection(Int32.Parse(numberOfQuestionsAskedNumericUpDown.Text), qnaDropdownComboBox.Text);
            SquizManager.Instance.Setup(Int32.Parse(numberOfQuestionsAskedNumericUpDown.Text), qnaDropdownComboBox.Text);

            //while (SquizManager.Instance.QNASubmapping.Count != 0)
            //{
            //    QuestionForm questionForm = new(SquizManager.Instance.CurrentQNA);
            //    questionForm.FormClosed += (sender, e) => this.Close();
            //    questionForm.Show();
            //}
            this.Hide();
            QuestionForm questionForm = new(SquizManager.Instance.CurrentQNA);
            questionForm.FormClosed += (sender, e) => this.Close();
            questionForm.Show();


            //foreach(var qna in liveQNA)
            //{
            //    QuestionForm questionForm = new(qna.Value);
            //    questionForm.FormClosed += (sender, e) => this.Close();
            //    questionForm.Show();
            //}

            //this.Hide();
            //QuestionForm questionForm = new(); // TODO: Pass in generated questions
            //questionForm.FormClosed += (sender, e) => this.Close();
            //questionForm.Show();
        }

        private void generateQNAList(string qnaDropdownComboBoxText, int numberOfQuestionsAskedNumericUpDown)
        {

        }
    }
}
