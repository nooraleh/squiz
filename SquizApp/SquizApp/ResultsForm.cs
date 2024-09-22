using QNALibrary;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace SquizApp
{
    public partial class ResultsForm : Form
    {
        public ResultsForm()
        {
            InitializeComponent();
            Display_amountCorrectFirstTryTextBox();
        }

        private void backToMainFormButton_Click(object sender, EventArgs e)
        {
            // Since a reshowing of `MainForm` instance is linked to the closing of a [Manual|Random|Replayer]Form,
            // which is turn linked to the closing of a CompareAnswerForm and furthermore this form, simply
            // closing `this` will cause the MainForm instance that was hidden to reappear
            this.Close();
        }

        private async void ResultsForm_Load(object sender, EventArgs e)
        {
            if (SquizManager.Instance.FailedQNAMappingQueue.Count > 0)
            {
                InitiateProgressBarAndStatusLabel();
                await Task.Run(() => LogFailedQNA());
                EndProgressBarAndStatusLabel();
            }
            else
            {
                loggingStatusLabel.Text = "";
            }
        }

        private void Display_amountCorrectFirstTryTextBox()
        {
            int amountFailed = SquizManager.Instance.FailedQNAMappingQueue.Count;
            int totalQuestions = SquizManager.Instance.NQuestions;
            amountCorrectFirstTryTextBox.Text = $"{amountFailed}/{totalQuestions}";
        }


        private void LogFailedQNA()
        {
            SquizManager.Instance.LogFailedQNA();
        }

        private void InitiateProgressBarAndStatusLabel()
        {
            loggingStatusLabel.Text = "Logging Failed QNA...";
            failedQNALoggingProgressBar.Style = ProgressBarStyle.Marquee;
            failedQNALoggingProgressBar.MarqueeAnimationSpeed = 30;
        }

        private void EndProgressBarAndStatusLabel()
        {
            loggingStatusLabel.Text = "Failed QNA logged!";
            failedQNALoggingProgressBar.Style = ProgressBarStyle.Blocks;
            failedQNALoggingProgressBar.Value = 100;
        }
    }
}
