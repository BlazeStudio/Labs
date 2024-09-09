using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace LR6
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        private void button1_Click(object sender, EventArgs e)
        {
            int a, n, x, i;
            double s, p;
            n = Convert.ToInt32(textBox1.Text);
            x = Convert.ToInt32(textBox2.Text);
            a = -1;
            p = 0;
            s = p;
            for (i = 0; i <= n; i++)
            {
                if (i % 2 == 1)
                    p = -1 * (x / 2);
                else
                    p = x / 2;
                s = s + p;
            }            
	MessageBox.Show("S = " + Convert.ToString(s), "Результат: ", MessageBoxButtons.YesNoCancel, MessageBoxIcon.Warning, MessageBoxDefaultButton.Button1);
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            textBox1.Text = Microsoft.VisualBasic.Interaction.InputBox("Input n", "n = ", "");
            textBox2.Text = Microsoft.VisualBasic.Interaction.InputBox("Input x", "x = ", "");

        }
        private void label1_Click(object sender, EventArgs e)
        {
            textBox1.Text = Microsoft.VisualBasic.Interaction.InputBox("Input n", "n = ", "");
        }
        private void label2_Click(object sender, EventArgs e)
        {
            textBox2.Text = Microsoft.VisualBasic.Interaction.InputBox("Input x", "x = ", "");
        }
    }
}
