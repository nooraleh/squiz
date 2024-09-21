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

    }
}
