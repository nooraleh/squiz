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
    public partial class QuestionForm : Form
    {
        public QuestionForm()
        {
            InitializeComponent();
            questionLabel.Text = SquizManager.Instance.Question();
            this.Text = SquizManager.Instance.Index();
            SetViewQuestionSnippetButton();
            SetViewImageSnippetButton();
        }

        private void SetViewImageSnippetButton()
        {
            bool shouldRevealViewImageSnippetButton = !(SquizManager.Instance.ImageQ() == string.Empty);
            viewImageButton.Visible = shouldRevealViewImageSnippetButton;
        }

        private void SetViewQuestionSnippetButton()
        {
            bool shouldRevealViewQuestionSnippetButton = !(SquizManager.Instance.SnippetQ() == string.Empty);
            viewQuestionSnippetButton.Visible = shouldRevealViewQuestionSnippetButton;
        }

        private void compareAnswerButton_Click(object sender, EventArgs e)
        {
            // save user answer
            SquizManager.Instance.AddUserAnswer(quizeeAnswerTextBox.Text);

            this.Hide();
            CompareAnswerForm compareAnswerForm = new(); // TODO: Pass in generated questions
            compareAnswerForm.FormClosed += (sender, e) => this.Close();
            compareAnswerForm.Show();
        }

        private void viewQuestionSnippetButton_Click(object sender, EventArgs e)
        {
            Utility.DisplayLatexPDF(GenerateTexFileName());
        }

        private string GenerateTexFileName()
        {
            return Utility.FullTextFilePath(@$"{SquizManager.Instance.Title}-{SquizManager.Instance.ID()}-{SquizManager.Instance.Index()}-snippetQ.tex");
        }

        private void viewImageButton_Click(object sender, EventArgs e)
        {
            ImageForm imageForm = new(SquizManager.Instance.ImageQ());
            imageForm.Show();
        }
    }
}
