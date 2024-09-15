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
    public partial class ManualModeForm : Form
    {
        public ManualModeForm()
        {
            InitializeComponent();

            Imply_ManualModeForm_Logic();
        }

        private void Imply_ManualModeForm_Logic()
        {
            Populate_qnaDropdownComboBox();
            Populate_testQNADropdownComboBox();
            Populate_qnaRangeNumericUpDowns();
            Populate_testQNARangeNumericUpDowns();
        }

        private void Populate_qnaDropdownComboBox()
        {
            QNACollection qnaCollection = new QNACollection();
            qnaDropdownComboBox.DataSource = new BindingSource(QNACollection.qnaCollectionMapping, null);
            qnaDropdownComboBox.DisplayMember = "Key";
            qnaDropdownComboBox.ValueMember = "Value";
        }

        private void Populate_testQNARangeNumericUpDowns()
        {
            if (Utility.IsDebugMode())
            {
                QNABase? currentlySelectedQNA = testQNADropdownComboBox.SelectedValue as QNABase;

                if (currentlySelectedQNA != null)
                {
                    // set the maximum for `qnaEndRangeNumericUpDown` to the current selection's
                    // underlying qnaMapping's Count
                    testQNAEndRangeNumericUpDown.Maximum = (decimal)currentlySelectedQNA.Count;
                    testQNAEndRangeNumericUpDown.Value = (decimal)currentlySelectedQNA.Count;

                    // start maximum to be the end range maximum minus 1
                    testQNAStartRangeNumericUpDown.Maximum = (testQNAEndRangeNumericUpDown.Maximum - 1M);
                }
            }
        }

        private void Populate_qnaRangeNumericUpDowns()
        {
            QNABase? currentlySelectedQNA = qnaDropdownComboBox.SelectedValue as QNABase;

            if (currentlySelectedQNA != null)
            {
                // set the maximum for `qnaEndRangeNumericUpDown` to the current selection's
                // underlying qnaMapping's Count
                qnaEndRangeNumericUpDown.Maximum = (decimal)currentlySelectedQNA.Count;
                qnaEndRangeNumericUpDown.Value = (decimal)currentlySelectedQNA.Count;

                // start maximum to be the end range maximum minus 1
                qnaStartRangeNumericUpDown.Maximum = (qnaEndRangeNumericUpDown.Maximum - 1M);
            }
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

        private void Impl_startQuizButton_Click()
        {
            if (useTestQNACheckBox.Checked)
            {
                int startRange = Int32.Parse(testQNAStartRangeNumericUpDown.Text);
                int endRange = Int32.Parse(testQNAEndRangeNumericUpDown.Text);
                SquizManager.Instance.ManualSetup(startRange, endRange, testQNADropdownComboBox.Text, new QNATestCollection());
            }
            else
            {
                int startRange = Int32.Parse(qnaStartRangeNumericUpDown.Text);
                int endRange = Int32.Parse(qnaEndRangeNumericUpDown.Text);
                SquizManager.Instance.ManualSetup(startRange, endRange, qnaDropdownComboBox.Text, new QNACollection());
            }
        }

        private void qnaDropdownComboBox_SelectedIndexChanged(object sender, EventArgs e)
        {
            Populate_qnaRangeNumericUpDowns();
        }

        private void testQNADropdownComboBox_SelectedIndexChanged(object sender, EventArgs e)
        {
            Populate_testQNARangeNumericUpDowns();
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
