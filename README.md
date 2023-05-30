代码片段
1、使用python编写程序实现的搜索文件夹里面所有文件包括子目录文件，将文件内容包含primarykey的行内容写入到csv文件里面


如果您的系统内存为16 GB，您可以尝试修改Solaris 10的内核参数以优化系统性能。以下是一些可能有用的内核参数设置： 
 1. 修改 shared memory 的大小： 
    set shmsys:shminfo_shmmax=4294967296 
    set shmsys:shminfo_shmmin=1 
    set shmsys:shminfo_shmmni=4096 
    set shmsys:shminfo_shmseg=1024 
 2. 增加最大文件句柄数： 
    set rlim_fd_max=65536 
    set rlim_fd_cur=65536 
 3. 增加最大线程数： 
    set maxusers=4096 
    set max_nprocs=30000 
 4. 增加系统缓冲区大小： 
    set msgsys:msginfo_msgmax=65536 
    set msgsys:msginfo_msgmnb=65536 
    set msgsys:msginfo_msgmni=4096 
    set msgsys:msginfo_msgseg=1024 
 5. 增加共享内存段的数量： 
    set semsys:seminfo_semmni=4096 
    set semsys:seminfo_semmsl=4096 
    set semsys:seminfo_semmns=8192 
 请注意，这些设置可能需要根据您的系统和应用程序的需要进行调整。在修改内核参数之前，请确保备份 /etc/system 文件，并了解每个参数的含义和影响。如果您不确定如何更改内核参数，请咨询系统管理员或其他有经验的专业人员。

修改之后如何生效

Share icon
在 Solaris 10 中修改内核参数后，可以通过以下方法使其生效： 
 1. 重新启动系统：在系统重启后，新的内核参数将在启动时生效。 
 2. 执行 sysctl 命令：使用 sysctl 命令重新加载内核参数。例如，要重新加载 rlim_fd_max 参数，可以使用以下命令： 
     $ sysctl -w rlim_fd_max=65536 
 3. 执行 sysdef 命令：使用 sysdef 命令检查新的内核参数是否已生效。例如，可以使用以下命令检查新的 rlim_fd_max 参数值： 
     $ sysdef | grep rlim_fd_max 
      rlim_fd_max = 65536 
 请注意，使用 sysctl 命令重新加载内核参数可能会导致某些进程被杀死，因为它们可能会使用新的限制。在重新加载内核参数之前，请确保您已备份任何重要数据，并将系统设置为最小化对业务的影响。
