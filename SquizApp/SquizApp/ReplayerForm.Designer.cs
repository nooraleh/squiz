namespace SquizApp
{
    partial class ReplayerForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
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
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            qnaLogsLabel = new Label();
            qnaLogsDropdownComboBox = new ComboBox();
            startQuizButton = new Button();
            squizSetupProgressBar = new ProgressBar();
            backToMainFormButton = new Button();
            SuspendLayout();
            // 
            // qnaLogsLabel
            // 
            qnaLogsLabel.AutoSize = true;
            qnaLogsLabel.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            qnaLogsLabel.Location = new Point(123, 82);
            qnaLogsLabel.Name = "qnaLogsLabel";
            qnaLogsLabel.Size = new Size(81, 21);
            qnaLogsLabel.TabIndex = 7;
            qnaLogsLabel.Text = "QNA Logs";
            // 
            // qnaLogsDropdownComboBox
            // 
            qnaLogsDropdownComboBox.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            qnaLogsDropdownComboBox.FormattingEnabled = true;
            qnaLogsDropdownComboBox.Location = new Point(123, 132);
            qnaLogsDropdownComboBox.Name = "qnaLogsDropdownComboBox";
            qnaLogsDropdownComboBox.Size = new Size(502, 29);
            qnaLogsDropdownComboBox.TabIndex = 8;
            // 
            // startQuizButton
            // 
            startQuizButton.Font = new Font("Segoe UI", 14.25F, FontStyle.Regular, GraphicsUnit.Point, 0);
            startQuizButton.Location = new Point(123, 368);
            startQuizButton.Name = "startQuizButton";
            startQuizButton.Size = new Size(244, 64);
            startQuizButton.TabIndex = 9;
            startQuizButton.Text = "Start Quiz!";
            startQuizButton.UseVisualStyleBackColor = true;
            startQuizButton.Click += startQuizButton_Click;
            // 
            // squizSetupProgressBar
            // 
            squizSetupProgressBar.Location = new Point(123, 466);
            squizSetupProgressBar.Name = "squizSetupProgressBar";
            squizSetupProgressBar.Size = new Size(718, 23);
            squizSetupProgressBar.TabIndex = 10;
            // 
            // backToMainFormButton
            // 
            backToMainFormButton.Font = new Font("Segoe UI", 14.25F, FontStyle.Regular, GraphicsUnit.Point, 0);
            backToMainFormButton.Location = new Point(597, 368);
            backToMainFormButton.Name = "backToMainFormButton";
            backToMainFormButton.Size = new Size(244, 64);
            backToMainFormButton.TabIndex = 11;
            backToMainFormButton.Text = "Back to Main";
            backToMainFormButton.UseVisualStyleBackColor = true;
            backToMainFormButton.Click += backToMainFormButton_Click;
            // 
            // ReplayerForm
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(956, 551);
            Controls.Add(backToMainFormButton);
            Controls.Add(squizSetupProgressBar);
            Controls.Add(startQuizButton);
            Controls.Add(qnaLogsDropdownComboBox);
            Controls.Add(qnaLogsLabel);
            Name = "ReplayerForm";
            Text = "ReplayerForm";
            FormClosed += ReplayerForm_FormClosed;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label qnaLogsLabel;
        private ComboBox qnaLogsDropdownComboBox;
        private Button startQuizButton;
        private ProgressBar squizSetupProgressBar;
        private Button backToMainFormButton;
    }
}