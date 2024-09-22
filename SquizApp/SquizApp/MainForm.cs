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
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }

        private void randomModeButton_Click(object sender, EventArgs e)
        {
            this.Hide();

            // create and display RandomModeForm
            RandomModeForm randomModeForm = new(this);
            randomModeForm.Show();
        }

        private void manualModeButton_Click(object sender, EventArgs e)
        {
            this.Hide();

            // create and display ManualModeForm
            ManualModeForm manualModeForm = new();
            manualModeForm.FormClosed += (sender, e) => this.Close();
            manualModeForm.Show();
        }

        private void replayerModeButton_Click(object sender, EventArgs e)
        {
            this.Hide();

            // create and display ReplayerModeForm
            ReplayerForm replayerModeForm = new(this);
            replayerModeForm.Show();
        }
    }
}
