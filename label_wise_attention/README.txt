-----------------------------------------------------------

EMNLP 2018 submission:

"Interpretable Emoji Prediction via Multi-Attention LSTMs"

-----------------------------------------------------------

Unzip the folder before opening any file.

The folder includes two files, one to show the single-attention networks and one for the multi-label attention network.

* The file “50_single_attention.html” includes 300 random examples from our corpus, along with gold label (G:) and 15 predictions (P:) of the single attention network. Each word of each tweet is highlighted with the weights alpha. 

* The file “50_multi_attention.html” includes the same set of tweets, with the emojis from the gold standard (G:) and the predictions (P:) of the multi label attention network. Moreover, by clicking on the emojis on the top, or on the predictions, it is possible to show the attention weights alpha_l of each label. Note that the words highlighted correspond the emoji displayed on the top left ("Selected")

In both files, the words in red font are out of vocabolary words.

