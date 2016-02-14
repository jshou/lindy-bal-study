lindy-bal-study
===============

Collection of data and scripts used in lindy/bal study

(Oh yeah, everything is python3)


Results
-------
`results.csv` contains the results of the survey. Each numbered row represents
the votes for a given song, and each column is the vote for a particular
participant. Votes are one of l, b, 2 or 0 for lindy, bal, both or neither.

Attributes
----------
`attributes.csv` contains the 5 binary features for each song hand labeled by
Josh. We'll be using the features as potential predictors of whether not a song
is bal/lindy danceable. The features are as follows:

* Triplety-swing
* Strong backbeat
* Melody with accents
* Big band
* Crashy ride/hihat
