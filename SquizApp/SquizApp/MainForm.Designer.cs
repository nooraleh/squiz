namespace SquizApp
{
    partial class MainForm
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            QNADropdownComboBox = new ComboBox();
            SuspendLayout();
            // 
            // QNADropdownComboBox
            // 
            QNADropdownComboBox.FormattingEnabled = true;
            QNADropdownComboBox.Items.AddRange(new object[] { "MockQNA1", "MockQNA2" });
            QNADropdownComboBox.Location = new Point(362, 88);
            QNADropdownComboBox.Name = "QNADropdownComboBox";
            QNADropdownComboBox.Size = new Size(277, 23);
            QNADropdownComboBox.TabIndex = 0;
            // 
            // MainForm
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1171, 702);
            Controls.Add(QNADropdownComboBox);
            Name = "MainForm";
            Text = "Squiz";
            ResumeLayout(false);
        }

        #endregion

        private ComboBox QNADropdownComboBox;
    }
}
