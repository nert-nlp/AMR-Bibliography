# AMR Bibliography

See http://people.cs.georgetown.edu/nschneid/cosc672/s17/amr-papers.html


Collected from http://amr.isi.edu/research.html (and suggestions from Jeff Flanigan), loosely organized by topic, and updated to 24 Aug 2017. A few selected papers are in bold.
The course readings will draw from this list as well as other sources.

###Overviews
“Abstract Meaning Representation: a survey” (Melanie Tosik), Jul. 9, 2015. Manuscript. PDF
Tutorial: “The Logic of AMR: Practical, Unified, Graph-Based Sentence Semantics for NLP” (Nathan Schneider, Jeffrey Flanigan, and Tim O’Gorman), NAACL-HLT, May 31, 2015. URL

###Annotation Scheme
"Abstract Meaning Representation for Sembanking" (L. Banarescu, C. Bonial, S. Cai, M. Georgescu, K. Griffitt, U. Hermjakob, K. Knight, P. Koehn, M. Palmer, and N. Schneider), Proc. Linguistic Annotation Workshop, 2013. PDF.
[guidelines] “Abstract Meaning Representation (AMR) 1.2.2 Specification” (L. Banarescu, C. Bonial, S. Cai, M. Georgescu, K. Griffitt, U. Hermjakob, K. Knight, P. Koehn, M. Palmer, and N. Schneider), Sep. 18, 2015. URL
“AMR Annotation Dictionary” (maintained by Ulf Hermjakob). URL
AMR Editor (annotation tool, built and maintained by Ulf Hermjakob). URL
“AMR Editor: A tool to build Abstract Meaning Representations”, Ulf Hermjakob. Manuscript. PDF
"Squib: Expressive Power of Abstract Meaning Representations" (Johan Bos), Computational Linguistics 42(3), 2016. PDF

###Multilingual
"Not an Interlingua, but Close: Comparison of English AMRs to Chinese and Czech" (N. Xue, O. Bojar, J. Hajic, M. Palmer, Z. Uresova, X. Zhang). Proc. LREC, 2014. PDF. 
"Annotating the Little Prince with Chinese AMRs", B. Li, Y. Wen, L. Bu, W. Qu, and N. Xue, Proc. 10th Linguistic Annotation Workshop (LAW X), 2016 PDF
"An AMR parser for English, French, German, Spanish and Japanese and a new AMR-annotated corpus" (Lucy Vanderwende, Arul Menezes and Chris Quirk), Proc. NAACL (Demo session), 2015. PDF
"Cross-lingual Abstract Meaning Representation Parsing" (Marco Damonte and Shay B. Cohen), arXiv. 2017.
"A Study Towards Spanish Abstract Meaning Representation" (Noelia Migueles-Abraira), MSc thesis, University of the Basque Country, 2017. PDF.

###Evaluation
"Smatch: an Evaluation Metric for Semantic Feature Structures," (S. Cai and K. Knight), Proc. ACL, 2013. PDF. 
"RIGA at SemEval-2016 Task 8: Impact of Smatch Extensions and Character-Level Neural Translation on AMR Parsing Accuracy" (Guntis Barzdins; Didzis Gosko), Proc. SemEval 2016. PDF Eval code
"An Incremental Parser for Abstract Meaning Representation" (M. Damonte, S. B. Cohen, G. Satta), Proc. EACL 2017/arXiv. Parser code, 

###Eval code
###Alignment
"Aligning English Strings with Abstract Meaning Representation Graphs" (Nima Pourdamghani, Yang Gao, Ulf Hermjakob and Kevin Knight), Proc. EMNLP, 2014. PDF dev data test data
"Learning to Map Dependency Parses to Abstract Meaning Representations" (Wei-Te Chen), ACL-IJCNLP Student Research Workshop. 2015. PDF
"Unsupervised AMR-Dependency Parse Alignment" (Wei-Te Chen and Martha Palmer), Proc. EACL 2017. PDF
"Supervised Syntax-based Alignment between English Sentences and Abstract Meaning Representation Graphs" (Chenhui Chu and Sadao Kurohashi), arXiv. 2017.
"AMRICA: an AMR Inspector for Cross-language Alignments" (Naomi Saphra and Adam Lopez), Proc. NAACL (Demo session), 2015. PDF 

##Parsing

###Shared Task Overview
"SemEval-2016 Task 8: Meaning Representation Parsing" (Jonathan May), Proc. SemEval 2016. PDF

###Transition-based
"A Transition-based Algorithm for AMR Parsing" (Chuan Wang, Nianwen Xue, Sameer Pradhan), Proc. NAACL, 2015. PDF
"CAMR at SemEval-2016 Task 8: An Extended Transition-based AMR Parser" (Chuan Wang; Sameer Pradhan; Xiaoman Pan; Heng Ji; Nianwen Xue), Proc. SemEval 2016. PDF
[+ neural] "An Incremental Parser for Abstract Meaning Representation" (M. Damonte, S. B. Cohen, G. Satta), Proc. EACL 2017/arXiv. Parser code, Eval code
"AMR Parsing with an Incremental Joint Model" (J. Zhou, F. Xu, H. Uszkoreit, W. Qu, R. Li and Y. Gu), Proc. EMNLP 2016. PDF 
"Boosting Transition-based AMR Parsing with Refined Actions and Auxiliary Analyzers" (C. Wang, N. Xue, and S. Pradhan), Proc. ACL, 2015. PDF
"Semantic Structure Analysis of Noun Phrases using Abstract Meaning Representation" (Y. Sawai, H. Shindo, and Y. Matsumoto), Proc. ACL, 2015. PDF

###Neural Networks
"RIGA at SemEval-2016 Task 8: Impact of Smatch Extensions and Character-Level Neural Translation on AMR Parsing Accuracy" (Guntis Barzdins; Didzis Gosko), Proc. SemEval 2016. PDF
"CU-NLP at SemEval-2016 Task 8: AMR Parsing using LSTM-based Recurrent Neural Networks" (William Foland; James H. Martin), Proc. SemEval 2016. PDF
[+ transition-based] "M2L at SemEval-2016 Task 8: AMR Parsing with Neural Networks" (Yevgeniy Puzikov; Daisuke Kawahara; Sadao Kurohashi), Proc. SemEval 2016. PDF 
"Addressing the Data Sparsity Issue in Neural AMR Parsing" (Xiaochang Peng, Chuan Wang, Daniel Gildea, and Nianwen Xue), Proc. EACL 2017. draft PDF
[+ transition-based] "Robust Incremental Neural Semantic Graph Parsing" (Jan Buys and Phil Blunsom), Proc. ACL/arXiv. 2017.
"Neural AMR: Sequence-to-Sequence Models for Parsing and Generation" (Ioannis Konstas, Srinivasan Iyer, Mark Yatskar, Yejin Choi, and Luke Zettlemoyer), Proc. ACL/arXiv. 2017.
"Abstract Meaning Representation Parsing using LSTM Recurrent Neural Networks" (William Foland and James H. Martin), Proc. ACL. 2017.
"Neural Semantic Parsing by Character-based Translation: Experiments with Abstract Meaning Representations" (Rik van Noord and Johan Bos), arXiv. 2017.
[+ transition-based] "AMR Parsing using Stack-LSTMs" (Miguel Ballesteros and Yaser Al-Onaizan), Proc. EMNLP/arXiv. 2017.
[+ transition-based] "Getting the Most out of AMR Parsing" (Chuan Wang and Nianwen Xue), Proc. EMNLP 2017. PDF

###Graph-based
"A Discriminative Graph-Based Parser for the Abstract Meaning Representation" (J. Flanigan, S. Thomson, J. Carbonell, C. Dyer, N. Smith). Proc. ACL, 2014. PDF 
"CMU at SemEval-2016 Task 8: Graph-based AMR Parsing with Infinite Ramp Loss" (Jeffrey Flanigan; Chris Dyer; Noah A. Smith; Jaime Carbonell), Proc. SemEval 2016. PDF
"Robust Subgraph Generation Improves Abstract Meaning Representation Parsing" (K. Werling, G. Angeli, and C. Manning), Proc. ACL, 2015. PDF

###Imitation Learning/Learning to Search
[+ transition-based] "Noise Reduction and Targeted Exploration in Imitation Learning for Abstract Meaning Representation Parsing" (J. Goodman, A. Vlachos, and J. Naradowsky), Proc. ACL. 2016. PDF
[+ transition-based] "UCL+Sheffield at SemEval-2016 Task 8: Imitation learning for AMR parsing with an alpha-bound" (James Goodman; Andreas Vlachos; Jason Naradowsky), Proc. SemEval 2016. PDF
[+ graph-based] "CLIP@UMD at SemEval-2016 Task 8: Parser for Abstract Meaning Representation using Learning to Search" (Sudha Rao; Yogarshi Vyas; Hal Daumé III; Philip Resnik), Proc. SemEval 2016. PDF

###Machine Translation Machinery
"Using Syntax-Based Machine Translation to Parse English into Abstract Meaning Representation" (M. Pust, U. Hermjakob, K. Knight, D. Marcu, J. May), Proc. EMNLP, 2015. PDF

###Graph Grammar Formalisms
"Semantics-Based Machine Translation with Hyperedge Replacement Grammars," (B. Jones, J. Andreas, D. Bauer, K-M. Hermann, and K. Knight), Proc. COLING, 2012. PDF. 
"Parsing Graphs with Hyperedge Replacement Grammars," (D. Chiang, J. Andreas, D. Bauer, K. M. Hermann, B. Jones, and K. Knight), Proc. ACL, 2013. PDF.
"Mapping between English Strings and Reentrant Semantic Graphs" (F. Braune, D. Bauer, and K. Knight), Proc. LREC, 2014. PDF.
"A Synchronous Hyperedge Replacement Grammar based approach for AMR parsing" (X. Peng, L. Song, and D. Gildea), Proc. CoNLL, 2015. PDF 
"Between a Rock and a Hard Place -- Uniform Parsing for Hyperedge Replacement DAG Grammars" (H. Björklund, F. Drewes, P. Ericson), Proc. LATA. 2016 PDF
"UofR at SemEval-2016 Task 8: Learning Synchronous Hyperedge Replacement Grammar for AMR Parsing" (Xiaochang Peng; Daniel Gildea), Proc. SemEval 2016. PDF
"Graph parsing with s-graph grammars" (J. Groschwitz, A. Koller, C. Teichmann), Proc. ACL, 2015. PDF

###Grammars: CCG
"Broad-coverage CCG Semantic Parsing with AMR" (Y. Artzi, K. Lee, and L. Zettlemoyer), Proc. EMNLP, 2015. PDF 
"Neural Shift-Reduce CCG Semantic Parsing" (Dipendra Kumar Misra and Yoav Artzi), Proc. EMNLP, 2016. PDF Supplement 

###Conversion from other syntactic/semantic formalisms
"An AMR parser for English, French, German, Spanish and Japanese and a new AMR-annotated corpus" (Lucy Vanderwende, Arul Menezes and Chris Quirk), Proc. NAACL (Demo session), 2015. PDF
"The Meaning Factory at SemEval-2016 Task 8: Producing AMRs with Boxer" (Johannes Bjerva; Johan Bos; Hessel Haagsma), Proc. SemEval 2016. PDF
"DynamicPower at SemEval-2016 Task 8: Processing syntactic parse trees with a Dynamic Semantics core" (Alastair Butler), Proc. SemEval 2016. PDF
"ICL-HD at SemEval-2016 Task 8: Meaning Representation Parsing - Augmenting AMR Parsing with a Preposition Semantic Role Labeling Neural Network" (Lauritz Brandt; David Grimm; Mengfei Zhou; Yannick Versley), Proc. SemEval 2016. PDF
Generation & Summarization
"Toward Abstractive Summarization Using Semantic Representations" (Fei Liu, Jeffrey Flanigan, Sam Thomson, Norman Sadeh, Noah A. Smith), Proc. NAACL. 2015. PDF
"Generating English from Abstract Meaning Representations" (Nima Pourdamghani, Kevin Knight, and Ulf Hermjakob). Proc. of INLG. 2016. PDF
"Neural Headline Generation on Abstract Meaning Representation", S. Takase, J. Suzuki, N. Okazaki, T. Hirao, M. Nagata, Proc. EMNLP. 2016. PDF
"AMR-to-text generation as a Traveling Salesman Problem" (L. Song, Y. Zhang, X. Peng, Z. Wang and D. Gildea), Proc. EMNLP. 2016. PDF
"Generation from Abstract Meaning Representation using Tree Transducers" (J. Flanigan, C. Dyer, N. A. Smith and J. Carbonell), Proc. NAACL. 2016. PDF
AMR-to-text Generation with Synchronous Node Replacement Grammar" (Linfeng Song, Xiaochang Peng, Yue Zhang, Zhiguo Wang, and Daniel Gildea), Proc. ACL/arXiv. 2017.
"Neural AMR: Sequence-to-Sequence Models for Parsing and Generation" (Ioannis Konstas, Srinivasan Iyer, Mark Yatskar, Yejin Choi, and Luke Zettlemoyer), Proc. ACL/arXiv. 2017.
"Transition-Based Generation from Abstract Meaning Representations" (Timo Schick), MSc thesis, Technische Universitat Dresden/arXiv. 2017.
"Text Summarization using Abstract Meaning Representation" (Shibhansh Dohare, Harish Karnick, and Vivek Gupta), arXiv. 2017.
Applications: Information Extraction, Question Answering, Biomedical
"Unsupervised Entity Linking with Abstract Meaning Representation" (Xiaoman Pan, Taylor Cassidy, Ulf Hermjakob, Heng Ji, Kevin Knight), Proc. NAACL, 2015. PDF
"Abstract Meaning Representation as Linked Data" (G. Burns, U. Hermjakob, J. L. Ambite), Proc. International Semantic Web Conference Resources Track. 2016. PDF
"Machine Comprehension Using Rich Semantic Representations" (M. Sachan, E. Xing), Proc. ACL. 2016. PDF
"Addressing a Question Answering Challenge by Combining Statistical Methods with Inductive Rule Learning and Reasoning" (A. Mitra, C. Baral), Proc. AAAI. 2016. PDF
"Extracting Biomolecular Interactions Using Semantic Parsing of Biomedical Text" (S. Garg, A. Galstyan, U. Hermjakob, and D. Marcu), Proc. AAAI, 2016. PDF
"Biomedical Event Extraction using Abstract Meaning Representation" (Sudha Rao, Daniel Marcu, Kevin Knight, Hal Daumé III), Proc. BioNLP, 2017. PDF
"Dependency and AMR Embeddings for Drug-Drug Interaction Extraction from Biomedical Literature" (Yanshan Wang, Sijia Liu, Majid Rastegar-Mojarad, Liwei Wang, Feichen Shen, Fei Liu, Hongfang Liu), Proc. ACM-BCB, 2017. PDF
