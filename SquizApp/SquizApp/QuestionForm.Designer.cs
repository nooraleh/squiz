﻿namespace SquizApp
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
            SuspendLayout();
            // 
            // questionLabel
            // 
            questionLabel.AutoSize = true;
            questionLabel.Font = new Font("Segoe UI", 24F, FontStyle.Regular, GraphicsUnit.Point, 0);
            questionLabel.Location = new Point(28, 24);
            questionLabel.Name = "questionLabel";
            questionLabel.Size = new Size(324, 45);
            questionLabel.TabIndex = 0;
            questionLabel.Text = "Question Placeholder";
            // 
            // quizeeAnswerTextBox
            // 
            quizeeAnswerTextBox.Font = new Font("Segoe UI", 24F, FontStyle.Regular, GraphicsUnit.Point, 0);
            quizeeAnswerTextBox.Location = new Point(28, 200);
            quizeeAnswerTextBox.Name = "quizeeAnswerTextBox";
            quizeeAnswerTextBox.Size = new Size(530, 50);
            quizeeAnswerTextBox.TabIndex = 1;
            // 
            // quizeeAnswerLabel
            // 
            quizeeAnswerLabel.AutoSize = true;
            quizeeAnswerLabel.Font = new Font("Segoe UI", 15.75F, FontStyle.Regular, GraphicsUnit.Point, 0);
            quizeeAnswerLabel.Location = new Point(28, 152);
            quizeeAnswerLabel.Name = "quizeeAnswerLabel";
            quizeeAnswerLabel.Size = new Size(68, 30);
            quizeeAnswerLabel.TabIndex = 2;
            quizeeAnswerLabel.Text = "label1";
            // 
            // QuestionForm
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
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
    }
}