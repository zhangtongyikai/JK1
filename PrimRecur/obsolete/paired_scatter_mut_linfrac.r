paired_scatter <- function(
  inDirName,
  graphicsFormat='png'
)
{
  
  if (graphicsFormat == 'png') {
    png(sprintf("%s/bubble/paired_scatter_mut.png", inDirName))
  } else if (graphicsFormat== 'pdf') {
    pdf(sprintf("%s/bubble/paired_scatter_mut.pdf", inDirName))
  }
  
  plot.new()
  par(mfrow=c(1,1))
  par(oma=c(1,1,1,1))
  par(mar=c(3,3,2,1))
  
  xSta = 0
  xEnd = 1
  
  lab = 'mutant allelic fraction'
  
  df = read.table(sprintf('%s/df_paired_mut.txt',inDirName),header=TRUE)
  df$val_p = df$p_mut / (df$p_mut + df$p_ref)
  df$val_r = df$r_mut / (df$r_mut + df$r_ref)
  df$delta = df$val_r-df$val_p
  df$color = 'black'
  df$color[df$geneN=='EGFR'] = 'red'
  df$color[df$geneN=='TP53'] = 'yellow'
  df$color[df$geneN=='IDH1'] = 'green'
  df$color[df$geneN=='MLH1'] = 'blue'
  df$color[df$geneN=='BRAF'] = 'grey'
  df$color[df$geneN=='PTEN'] = 'orange'
  
  df_ft = df[df$p_mut>1 | df$r_mut>1,]
  df_ft = df_ft[order(-abs(df_ft$delta)),]
  
  plot(c(),c(), xlim=c(xSta,xEnd), ylim=c(xSta,xEnd), axes=F,ann=F, xaxt='n',yaxt='n')
  par(new=T)

  symbols(x=df_ft$val_p, y=df_ft$val_r, circles=rep(0.015,nrow(df_ft)), inches=F, bg=df_ft$color, fg='black', xlim=c(xSta,xEnd), ylim=c(xSta,xEnd))
  par(new=T)
  
  plot(c(xSta,xEnd),c(xSta,xEnd), type='l', pch=22, lty=2, xlim=c(xSta,xEnd), ylim=c(xSta,xEnd), axes=F,ann=F, xaxt='n',yaxt='n')
  
  if (graphicsFormat=='png' || graphicsFormat=='pdf') {
    dev.off()
  }
}

inDirName = '/EQL1/PrimRecur/paired'
#   for (fmt in c('png','pdf','')) paired_scatter(inDirName,geneN,fmt)

paired_scatter(inDirName,'')