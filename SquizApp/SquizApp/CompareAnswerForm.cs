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
    public partial class CompareAnswerForm : Form
    {
        public CompareAnswerForm()
        {
            InitializeComponent();
            modelAnswerTextBox.Text = SquizManager.Instance.CurrentQNA["a"];
            userAnswerTextBox.Text = SquizManager.Instance.CurrentQNA["userA"];
        }

        private void userHappyButton_Click(object sender, EventArgs e)
        {
            SquizManager.Instance.CurrentQNAPass();
            NextPageForm();
        }


        private void NextPageForm()
        {
            // if we run out of QNA, then the ResultsForm
            // else we make a new QuestionForm with the next QNA

            // hide this page
            this.Hide();
            if (SquizManager.Instance.QNASubmapping.Count == 0)
            {
                ResultsForm resultsForm = new();
                resultsForm.FormClosed += (sender, e) => this.Close();
                resultsForm.Show();
            }
            else
            {
                QuestionForm questionForm = new();
                questionForm.FormClosed += (sender, e) => this.Close();
                questionForm.Show();
            }
        }

        private void userNotHappyButton_Click(object sender, EventArgs e)
        {
            SquizManager.Instance.CurrentQNAFail();
            NextPageForm();
        }
    }
}
