using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace Laba9_nechit
{
    public partial class Form1 : Form
    {
        int[] a = new int[1000];
        int[] b = new int[1000];
        public Form1()
        {
            InitializeComponent();
        }
        private void button1_Click(object sender, EventArgs e)
        {int n, i;
            string spisok;
            spisok = "";
            a = new int[1000];
            label4.Text = "";
            listBox1.Items.Clear();
            n = Convert.ToInt32(textBox2.Text);
            Random rnd = new Random();
            for (i = 1; i <= n; i++)
            {
                a[i] = rnd.Next(-100, 101);
                spisok = spisok + Convert.ToString(i) + ") " +
               Convert.ToString(a[i]) + " " + Environment.NewLine; // перевод строки
                b[i] = i * a[i];
                listBox1.Items.Add(Convert.ToString(i) + ")   " + Convert.ToString(b[i]));
            }
            label4.Text = spisok;
        }
    }
}
