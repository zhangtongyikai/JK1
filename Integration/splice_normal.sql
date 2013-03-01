drop table IF EXISTS splice_normal;
CREATE TABLE splice_normal (
	samp_id varchar(63) NOT NULL,
	loc1 varchar(31) NOT NULL, -- hg19
	loc2 varchar(31) NOT NULL,
	nReads mediumint unsigned NOT NULL,
	nPos tinyint unsigned NOT NULL,
	primary key (samp_id,loc1,loc2),
	index (samp_id,loc1),
	index (samp_id,loc2)
);

LOAD DATA LOCAL INFILE "/EQL1/NSL/RNASeq/alignment/splice_normal_NSL36.dat" INTO TABLE splice_normal;