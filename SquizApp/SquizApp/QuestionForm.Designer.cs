namespace SquizApp
{
    partial class QuestionForm
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
            questionLabel = new Label();
            quizeeAnswerTextBox = new TextBox();
            quizeeAnswerLabel = new Label();
            compareAnswerButton = new Button();
            SuspendLayout();
            // 
            // questionLabel
            // 
            questionLabel.AutoSize = true;
            questionLabel.Font = new Font("Segoe UI", 15.75F, FontStyle.Regular, GraphicsUnit.Point, 0);
            questionLabel.Location = new Point(28, 24);
            questionLabel.Name = "questionLabel";
            questionLabel.Size = new Size(211, 30);
            questionLabel.TabIndex = 0;
            questionLabel.Text = "Question Placeholder";
            // 
            // quizeeAnswerTextBox
            // 
            quizeeAnswerTextBox.Font = new Font("Segoe UI", 24F, FontStyle.Regular, GraphicsUnit.Point, 0);
            quizeeAnswerTextBox.Location = new Point(55, 511);
            quizeeAnswerTextBox.Multiline = true;
            quizeeAnswerTextBox.Name = "quizeeAnswerTextBox";
            quizeeAnswerTextBox.Size = new Size(1239, 198);
            quizeeAnswerTextBox.TabIndex = 1;
            // 
            // quizeeAnswerLabel
            // 
            quizeeAnswerLabel.AutoSize = true;
            quizeeAnswerLabel.Font = new Font("Segoe UI", 15.75F, FontStyle.Regular, GraphicsUnit.Point, 0);
            quizeeAnswerLabel.Location = new Point(55, 450);
            quizeeAnswerLabel.Name = "quizeeAnswerLabel";
            quizeeAnswerLabel.Size = new Size(133, 30);
            quizeeAnswerLabel.TabIndex = 2;
            quizeeAnswerLabel.Text = "Your Answer:";
            // 
            // compareAnswerButton
            // 
            compareAnswerButton.Location = new Point(549, 726);
            compareAnswerButton.Name = "compareAnswerButton";
            compareAnswerButton.Size = new Size(210, 66);
            compareAnswerButton.TabIndex = 3;
            compareAnswerButton.Text = "Compare to Model Answer";
            compareAnswerButton.UseVisualStyleBackColor = true;
            compareAnswerButton.Click += compareAnswerButton_Click;
            // 
            // QuestionForm
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1437, 819);
            Controls.Add(compareAnswerButton);
            Controls.Add(quizeeAnswerLabel);
            Controls.Add(quizeeAnswerTextBox);
            Controls.Add(questionLabel);
            Name = "QuestionForm";
            Text = "Question Form";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label questionLabel;
        private TextBox quizeeAnswerTextBox;
        private Label quizeeAnswerLabel;
        private Button compareAnswerButton;
    }
}