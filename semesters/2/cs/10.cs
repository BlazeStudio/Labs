using System.Collections.Generic; 
using System.ComponentModel; 
using System.Data;
using System.Drawing; 
using System.Linq; 
using System.Text;
using System.Threading.Tasks; 
using System.Windows.Forms;
namespace WindowsFormsApp10
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        private void button1_Click(object sender, EventArgs e)
        {
            int i, j, n, min; string spisok;
            int[] a = new int[1000];

            n = Convert.ToInt32(comboBox1.Text); spisok = "";
            listBox1.Text = "";

            for (i = 1; i <= n; i++)
            {
                a[i] = rnd.Next(-100, 101);
                Convert.ToString(a[i]) + "	" + Environment.NewLine;
            }
            label3.Text = spisok;
for (i = 1; i <= n - 1; i++)
            {
                for (j = i + 1; j <= n; j++)
                {
if (a[i] > a[j]) { min = a[j]; a[j] = a[i]; a[i] = min; }

                }
            } for (i = 1; i <= n; i++) { listBox1.Items.Add(Convert.ToString(i) + ")	" + Convert.ToString(a[i])); }
        }
    }


using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Reflection.Emit;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace Laba10_nechit
{
    public partial class Form1 : Form
    {
        int[] a = new int[1000];
        int[] b = new int[1000];
        public Form1()
        {
            InitializeComponent();
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            comboBox1.Items.AddRange(new string[] { "2", "3", "4", "5", "6", "7", "8", "9", "10" });
        }
        private void button1_Click(object sender, EventArgs e)
        {
            int n, i, d;
            string spisok;
            spisok = "";
            a = new int[1000];
            label4.Text = "";
            listBox1.Items.Clear();
            n = Convert.ToInt32(comboBox1.Text);
            d = Convert.ToInt32(textBox2.Text);
            if (d < 0)
            {
                DialogResult result = MessageBox.Show("Число B не должно быть отрицательным!", "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Warning, MessageBoxDefaultButton.Button1);
            }
            else
            {
                Random rnd = new Random();
                for (i = 1; i <= n; i++)
                {
                    a[i] = rnd.Next(-100, 101);
                    spisok = spisok + Convert.ToString(i) + ") " +
                   Convert.ToString(a[i]) + " " + Environment.NewLine; 
                    if (a[i] < d) { b[i] = a[i]; listBox1.Items.Add(Convert.ToString(i) + ")   " + Convert.ToString(b[i]));}
                }
                label4.Text = spisok;
            }
        }
    }
}
