using QNALibrary;

namespace SquizApp
{
    public partial class RandomModeForm : Form
    {
        public RandomModeForm(MainForm mainForm)
        {
            InitializeComponent();

            Populate_qnaDropdownComboBox();
            Populate_testQNADropdownComboBox();
            _mainForm = mainForm;
        }

        private MainForm _mainForm;

        private void Populate_qnaDropdownComboBox()
        {
            QNACollection qnaCollection = new QNACollection();
            qnaDropdownComboBox.DataSource = new BindingSource(QNACollection.qnaCollectionMapping, null);
            qnaDropdownComboBox.DisplayMember = "Key";
            qnaDropdownComboBox.ValueMember = "Value";
        }

        private void Populate_testQNADropdownComboBox()
        {
            // population and show if in DEBUG mode, hide if not
            if (Utility.IsDebugMode())
            {
                QNATestCollection qnaCollection = new QNATestCollection();
                testQNADropdownComboBox.DataSource = new BindingSource(QNATestCollection.qnaCollectionMapping, null);
                testQNADropdownComboBox.DisplayMember = "Key";
                testQNADropdownComboBox.ValueMember = "Value";
            }
            else
            {
                testQNADropdownComboBox.Visible = false;
                testQNADropdownLabel.Visible = false;
                useTestQNACheckBox.Visible = false;
            }
        }

        private async void startQuizButton_Click(object sender, EventArgs e)
        {
            Initiate_squizSetupProgressBar();
            await Task.Run(() => Impl_startQuizButton_Click());
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

        private void Impl_startQuizButton_Click()
        {
            if (useTestQNACheckBox.Checked)
            {
                SquizManager.Instance.RandomSetup(Int32.Parse(numberOfQuestionsAskedNumericUpDown.Text), testQNADropdownComboBox.Text, new QNATestCollection());
            }
            else
            {
                SquizManager.Instance.RandomSetup(Int32.Parse(numberOfQuestionsAskedNumericUpDown.Text), qnaDropdownComboBox.Text, new QNACollection());
            }
        }

        private void CleanSnippetsDirectory()
        {
            string snippetsDirectory = Utility.SnippetsDirectory();

            if (Directory.Exists(snippetsDirectory))
            {
                Directory.Delete(snippetsDirectory, true);
            }
        }

        private void backToMainFormButton_Click(object sender, EventArgs e)
        {
            _mainForm.Show();
            this.Hide();
        }

        private void RandomModeForm_FormClosed(object sender, FormClosedEventArgs e)
        {
            _mainForm.Show();
        }
    }
}
