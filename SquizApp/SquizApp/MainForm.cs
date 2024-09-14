using QNALibrary;

namespace SquizApp
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }

        private async  void startQuizButton_Click(object sender, EventArgs e)
        {
            Initiate_squizSetupProgressBar();
            await Task.Run(() => impl_startQuizButton_Click());
            End_squizSetupProgressBar();

            this.FormClosed += (sender, e) => CleanSnippetsDirectory();
            this.Hide();

            // creation and display first QuestionForm
            QuestionForm questionForm = new();
            questionForm.FormClosed += (sender, e) => this.Close();
            questionForm.Show();
        }

        private void Initiate_squizSetupProgressBar()
        {
            squizSetupProgressBar.Style = ProgressBarStyle.Marquee;
            squizSetupProgressBar.MarqueeAnimationSpeed = 30;
        }

        private void End_squizSetupProgressBar()
        {
            squizSetupProgressBar.Style = ProgressBarStyle.Blocks;
            squizSetupProgressBar.Value = 100;
        }

        private void impl_startQuizButton_Click()
        {
            SquizManager.Instance.Setup(Int32.Parse(numberOfQuestionsAskedNumericUpDown.Text), qnaDropdownComboBox.Text);
        }

        private void CleanSnippetsDirectory()
        {
            string snippetsDirectory = Utility.SnippetsDirectory();

            if (Directory.Exists(snippetsDirectory))
            {
                Directory.Delete(snippetsDirectory, true);
            }
        }

    }
}
