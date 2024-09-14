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
        }

        private void backToMainFormButton_Click(object sender, EventArgs e)
        {
            this.Hide();
            RandomModeForm mainForm = new();
            mainForm.Show();
            this.Close();
        }
    }
}
