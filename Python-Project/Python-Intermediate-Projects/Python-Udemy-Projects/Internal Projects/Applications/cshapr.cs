using System;
using System.Data;
using Microsoft.SqlServer.Dts.Runtime;
using System.Windows.Forms;
using System.IO;
using System.Linq;

DirectoryInfo yourRootDir = new DirectoryInfo(@"C:\Test\");
      foreach (FileInfo file in yourRootDir.GetFiles())
                if (file.LastWriteTime < DateTime.Now.AddDays(-0))
                    file.Delete();

