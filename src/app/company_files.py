import pandas as pd
import numpy as np

alpha = {
  'parseCols': 'B:H,M',
  'colNames': ['market','listdate','company','group','sector','subsector','country','marketcap']
}

beta = {
  'parseCols': 'A:F,H,M',
  'colNames': ['listdate','company','group','sector','subsector','country','market','marketcap']
}

charlie = {
  'parseCols': 'A:G,L',
  'colNames': ['listdate','company','group','sector','subsector','country','market','marketcap']
}

delta = {
  'parseCols': 'A:H',
  'colNames': ['listdate','company','group','sector','subsector','country','market','marketcap']
}

echo = {
  'parseCols': 'A:G,I',
  'colNames': ['listdate','company','group','sector','subsector','country','market','marketcap']
}

foxtrot = {
  # no group
  'parseCols': 'B:F,H,J',
  'colNames': ['listdate','company','sector','subsector','country','market','marketcap']
}

golf = {
  'parseCols': 'A:F,I,M',
  'colNames': ['listdate','company','group','sector','subsector','country','market','marketcap']
}

files = [
  { 
    'filename': 'LISTDATE HISTORIC 1999.XLS',
    'year': 1999,
    'sheets': [
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha }
    ]
  },
  {
    'filename': 'LISTDATE HISTORIC 2000.XLS',
    'year': 2000,
    'sheets': [
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha }
    ]
  },
  {
    'filename': 'LISTDATE HISTORIC 2001.XLS',
    'year': 2001,
    'sheets': [
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha }
    ]
  },
  {
    'filename': 'LISTDATE HISTORIC 2002.XLS',
    'year': 2002,
    'sheets': [
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha }
    ]
  },
  {
    'filename': 'LISTDATE HISTORIC 2003.XLS',
    'year': 2003,
    'sheets': [
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha }
    ]
  },
  {
    'filename': 'LISTDATE HISTORIC 2004.XLS',
    'year': 2004,
    'sheets': [
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha }
    ]
  },
  {
    'filename': 'LISTDATE HISTORIC 2005.XLS',
    'year': 2005,
    'sheets': [
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha }
    ]
  },
  {
    'filename': 'LISTDATE HISTORIC 2006.XLS',
    'year': 2006,
    'sheets': [
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha },
      { 'headerRow': 3, **alpha }
    ]
  },
  {
    'filename': 'LISTDATE HISTORIC 2007.XLS',
    'year': 2007,
    'sheets': [
      { 'headerRow': 6, **beta },
      { 'headerRow': 6, **beta },
      { 'headerRow': 6, **beta },
      { 'headerRow': 7, **golf },
      { 'headerRow': 7, **golf },
      { 'headerRow': 7, **golf },
      { 'headerRow': 6, **beta },
      { 'headerRow': 6, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta }
    ]
  },
  {
    'filename': 'LISTDATE HISTORIC 2008.XLS',
    'year': 2008,
    'sheets': [
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta }
    ]
  },
  {
    'filename': 'LISTDATE HISTORIC 2009.XLS',
    'year': 2009,
    'sheets': [
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta }
    ]
  },
  {
    'filename': 'LISTDATE HISTORIC 2010.XLS',
    'year': 2010,
    'sheets': [
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta }
    ]
  },
  {
    'filename': 'LISTDATE HISTORIC 2011.XLS',
    'year': 2011,
    'sheets': [
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta }
    ]
  },
  {
    'filename': 'LISTDATE HISTORIC 2012.XLS',
    'year': 2012,
    'sheets': [
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta }
    ]
  },
  {
    'filename': 'LISTDATE HISTORIC 2013 v1.xlsx',
    'year': 2013,
    'sheets': [
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **beta },
      { 'headerRow': 7, **charlie },
      { 'headerRow': 7, **charlie },
      { 'headerRow': 7, **charlie }
    ]
  },
  {
    'filename': 'LISTDATE HISTORIC 2014.xls',
    'year': 2014,
    'sheets': [
      { 'headerRow': 7, **charlie },
      { 'headerRow': 7, **charlie },
      { 'headerRow': 7, **charlie },
      { 'headerRow': 7, **charlie },
      { 'headerRow': 7, **charlie },
      { 'headerRow': 7, **charlie },
      { 'headerRow': 7, **charlie },
      { 'headerRow': 7, **charlie },
      { 'headerRow': 7, **charlie },
      { 'headerRow': 7, **charlie },
      { 'headerRow': 7, **charlie },
      { 'headerRow': 7, **charlie }
    ]
  },
  {
    'filename': 'LISTDATE HISTORIC 2015.xls',
    'year': 2015,
    'sheets': [
      { 'headerRow': 7, **delta },
      { 'headerRow': 7, **delta },
      { 'headerRow': 7, **delta },
      { 'headerRow': 7, **delta },
      { 'headerRow': 7, **delta },
      { 'headerRow': 7, **delta },
      { 'headerRow': 7, **delta },
      { 'headerRow': 7, **delta },
      { 'headerRow': 7, **delta },
      { 'headerRow': 7, **delta },
      { 'headerRow': 7, **delta },
      { 'headerRow': 7, **delta }
    ]
  },
  {
    'filename': 'LISTDATE HISTORIC 2016.xls',
    'year': 2016,
    'sheets': [
      { 'headerRow': 7, **delta },
      { 'headerRow': 7, **delta },
      { 'headerRow': 7, **delta },
      { 'headerRow': 7, **delta },
      { 'headerRow': 7, **delta },
      { 'headerRow': 7, **delta },
      { 'headerRow': 7, **delta },
      { 'headerRow': 7, **delta },
      { 'headerRow': 7, **delta },
      { 'headerRow': 7, **delta },
      { 'headerRow': 7, **delta },
      { 'headerRow': 7, **delta }
    ]
  },
  {
    'filename': 'COMPANY FILES HISTORIC 2017.xlsx',
    'year': 2017,
    'sheets': [
      { 'headerRow': 7, **delta },
      { 'headerRow': 6, **echo },
      { 'headerRow': 6, **echo },
      { 'headerRow': 6, **echo },
      { 'headerRow': 6, **echo },
      { 'headerRow': 6, **echo },
      { 'headerRow': 6, **echo },
      { 'headerRow': 6, **echo },
      { 'headerRow': 6, **echo },
      { 'headerRow': 6, **echo },
      { 'headerRow': 6, **echo },
      { 'headerRow': 6, **echo }
    ]
  },
  {
    'filename': 'COMPANY FILES HISTORIC 2018.xlsx',
    'year': 2018,
    'sheets': [
      { 'headerRow': 6, **foxtrot },
      { 'headerRow': 6, **foxtrot },
      { 'headerRow': 6, **foxtrot },
      { 'headerRow': 6, **foxtrot },
      { 'headerRow': 6, **foxtrot }
    ]
  }
]