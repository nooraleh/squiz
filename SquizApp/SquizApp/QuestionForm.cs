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
        }

        private void compareAnswerButton_Click(object sender, EventArgs e)
        {
            this.Hide();
            CompareAnswerForm compareAnswerForm = new(); // TODO: Pass in generated questions
            compareAnswerForm.FormClosed += (sender, e) => this.Close();
            compareAnswerForm.Show();
        }
    }
}
