using QNALibrary;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace SquizApp
{
    public partial class ReplayerForm : Form
    {
        public ReplayerForm()
        {
            InitializeComponent();
            Populate_qnaLogsDropdownComboBox();
        }

        private void Populate_qnaLogsDropdownComboBox()
        {
            string logsDirectory = Utility.LogsDirectory();

            string[] logFiles = Directory.GetFiles(logsDirectory, "*.json");

            if (logFiles.Length != 0)
            {
                foreach (var logFile in logFiles)
                {
                    qnaLogsDropdownComboBox.Items.Add(Path.GetFileName(logFile));
                }
            }
            else
            {
                qnaLogsLabel.Text = "No logs for the failed QNA - nothing to replay!";
                qnaLogsDropdownComboBox.Visible = false;
            }
        }

        private async void startQuizButton_Click(object sender, EventArgs e)
        {
            Initiate_squizSetupProgressBar();

            string fullPathToLogFile = DetermineSetupArgument();
            await Task.Run(() => Impl_startQuizButton_Click(fullPathToLogFile));

            End_squizSetupProgressBar();

            this.FormClosed += (sender, e) => CleanSnippetsDirectory();
            this.Hide();

            // creation and display first QuestionForm
            QuestionForm questionForm = new();
            questionForm.FormClosed += (sender, e) => this.Close();
            questionForm.Show();
        }

        private void CleanSnippetsDirectory()
        {
            string snippetsDirectory = Utility.SnippetsDirectory();

            if (Directory.Exists(snippetsDirectory))
            {
                Directory.Delete(snippetsDirectory, true);
            }
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

        private string DetermineSetupArgument()
        {
            string? fileName = qnaLogsDropdownComboBox.SelectedItem as string;

            if (fileName != null)
            {
                return Path.Combine(
                Utility.LogsDirectory(),
                fileName);
            }

            return string.Empty;
        }


        private void Impl_startQuizButton_Click(string fullPathToLogFile)
        {
            SquizManager.Instance.ReplayerSetup(fullPathToLogFile);
        }
    }
}
