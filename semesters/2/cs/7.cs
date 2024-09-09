using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace LR7
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            textBox1.Text = Microsoft.VisualBasic.Interaction.InputBox("Введите точность", "Точность = ", "0,001");
            label3.Text = "";
            label5.Text = "";
        }

        private void label2_Click(object sender, EventArgs e)
        {
            int n; 
            double s, sl, toch;
            toch = Convert.ToDouble(textBox1.Text);
            n = 1;
            sl = 1;
            s = 1;
            while (sl > toch)
            {
                n++;
                if (n % 2 == 0)
                {
                    sl = -1 * (1 / n);
                }
                if (n % 2 != 0)
                    sl = 1 / n
                s += sl;
                
            }
            label3.Text = Convert.ToString(s);
            label5.Text = Convert.ToString(n);
        }
    }
}
