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
            SquizManager.Instance.Setup(Int32.Parse(numberOfQuestionsAskedNumericUpDown.Text), qnaDropdownComboBox.Text);

            this.Hide();
            QuestionForm questionForm = new();
            questionForm.FormClosed += (sender, e) => this.Close();
            questionForm.Show();
        }

        private void generateQNAList(string qnaDropdownComboBoxText, int numberOfQuestionsAskedNumericUpDown)
        {

        }
    }
}
