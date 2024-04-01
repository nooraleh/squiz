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
            this.Hide();
            QuestionForm questionForm = new(); // TODO: Pass in generated questions
            questionForm.FormClosed += (sender, e) => this.Close();
            questionForm.Show();
        }
    }
}
