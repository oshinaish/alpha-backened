{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww28600\viewh16380\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # README.md\
# ---------\
# Budget PDF Extractor (FastAPI Backend)\
\
## Description\
This is a FastAPI backend service that accepts PDF uploads of bank statements and extracts raw transaction lines to assist with budgeting.\
\
## How to Run Locally\
\
```bash\
pip install -r requirements.txt\
uvicorn main:app --reload\
```\
\
## API Endpoint\
**POST** `/upload-pdf`\
- Accepts: PDF file as `file`\
- Returns: total transactions and sample extracted lines\
}