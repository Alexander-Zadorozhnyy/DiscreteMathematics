using System;
using System.Linq;
using System.Collections.Generic;

namespace Task_2_C
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] items = { "A", "U", "C", "G" };

            var query = from i1 in items from i2 in items from i3 in items from i4 in items 
                        from i5 in items from i6 in items from i7 in items from i8 in items
                        from i9 in items from i10 in items from i11 in items from i12 in items
                        from i13 in items from i14 in items from i15 in items
                        select i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9 + i10 + i11 + i12 + i13 + i14 + i15;

            string stop1 = "UAA", stop2 = "UGA", stop3 = "UAG";
            long count = 0;
            foreach (var result in query)
            {
                if (result.IndexOf(stop1) == -1 && result.IndexOf(stop2) == -1 && result.IndexOf(stop3) == -1)
                {
                    count++;
                    if (count % 500000 == 0)
                        Console.WriteLine(result);
                }
            }
            Console.WriteLine(count * 3); // 1620249447
            Console.ReadKey();
        }
        static void Main_s(string[] args)
        {
            List<string> all_items = new List<string>() { "AA", "AU", "AC", "AG", "UA", "UU", "UC", "UG", "CA", "CU", "CC", "CG", "GA", "GU", "GC", "GG" };
            for (int tryed = 0; tryed < 13; tryed++)
            {
                List<string> new_items = new List<string>();
                for (int i = 0; i < all_items.Count; i++)
                {
                    string el = all_items[i];
                    if (el[(el.Length - 2)..] == "UA")
                    {
                        new_items.Add(el + "U");
                        new_items.Add(el + "С");
                    }
                    else if (el[(el.Length - 2)..] == "UG")
                    {
                        new_items.Add(el + "G");
                        new_items.Add(el + "U");
                        new_items.Add(el + "С");
                    }
                    else
                    {
                        new_items.Add(el + "A");
                        new_items.Add(el + "G");
                        new_items.Add(el + "U");
                        new_items.Add(el + "С");
                    }
                }
                all_items = new_items;
                Console.WriteLine(tryed);
                Console.WriteLine(all_items[all_items.Count / 2]);
                Console.WriteLine(all_items.Count);
            }
            Console.WriteLine(all_items.Count * 3);
            Console.ReadKey();
        }
    }
}
