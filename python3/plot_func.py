from matplotlib import pyplot as plt

def timecourse(sim):
    plt.figure(figsize=(12,15))
    plt.rcParams['font.family'] = 'Arial'
    plt.rcParams['font.size'] = 10
    plt.rcParams['axes.linewidth'] = 1
    plt.rcParams['lines.linewidth'] = 2

    plt.subplots_adjust(wspace=0.4, hspace=0.5)

    plt.subplot(4,2,1)
    plt.plot(sim.t,sim.ERK_act[:,0]/589.5,'-',label='EGF=0 nM')
    plt.plot(sim.t,sim.ERK_act[:,3]/589.5,'--',label='EGF=0.5 nM')
    plt.plot(sim.t,sim.ERK_act[:,6]/589.5,':',label='EGF=10 nM')
    plt.title('EGF increasing HRG=0.5 nM')
    plt.xlim(0,1900)
    plt.xticks([0,500,1000,1500])
    plt.xlabel('Time (s)')
    plt.ylim(0,1.5)
    plt.yticks([0,0.5,1,1.5])
    plt.ylabel('Normalized ERK*')
    plt.legend(loc='upper right',fontsize=8)

    plt.subplot(4,2,2)
    plt.plot(sim.t,sim.ERK_act[:,1]/589.5,'-',label='EGF=0 nM')
    plt.plot(sim.t,sim.ERK_act[:,4]/589.5,'--',label='EGF=0.5 nM')
    plt.plot(sim.t,sim.ERK_act[:,7]/589.5,':',label='EGF=10 nM')
    plt.title('EGF increasing HRG=10 nM')
    plt.xlim(0,1900)
    plt.xticks([0,500,1000,1500])
    plt.xlabel('Time (s)')
    plt.ylim(0,1.5)
    plt.yticks([0,0.5,1,1.5])
    plt.ylabel('Normalized ERK*')
    plt.legend(loc='upper right',fontsize=8)

    plt.subplot(4,2,3)
    plt.plot(sim.t,sim.ERK_act[:,2]/589.5,'-',label='HRG=0 nM')
    plt.plot(sim.t,sim.ERK_act[:,3]/589.5,'--',label='HRG=0.5 nM')
    plt.plot(sim.t,sim.ERK_act[:,4]/589.5,':',label='HRG=10 nM')
    plt.title('EGF=0.5 nM HRG increasing')
    plt.xlim(0,1900)
    plt.xticks([0,500,1000,1500])
    plt.xlabel('Time (s)')
    plt.ylim(0,1.5)
    plt.yticks([0,0.5,1,1.5])
    plt.ylabel('Normalized ERK*')
    plt.legend(loc='upper right',fontsize=8)

    plt.subplot(4,2,4)
    plt.plot(sim.t,sim.ERK_act[:,5]/589.5,'-',label='HRG=0 nM')
    plt.plot(sim.t,sim.ERK_act[:,6]/589.5,'--',label='HRG=0.5 nM')
    plt.plot(sim.t,sim.ERK_act[:,7]/589.5,':',label='HRG=10 nM')
    plt.title('EGF=10 nM HRG increasing')
    plt.xlim(0,1900)
    plt.xticks([0,500,1000,1500])
    plt.xlabel('Time (s)')
    plt.ylim(0,1.5)
    plt.yticks([0,0.5,1,1.5])
    plt.ylabel('Normalized ERK*')
    plt.legend(loc='upper right',fontsize=8)

    plt.subplot(4,2,5)
    plt.plot(sim.t,sim.Akt_act[:,0]/18.8,'-',label='EGF=0 nM')
    plt.plot(sim.t,sim.Akt_act[:,3]/18.8,'--',label='EGF=0.5 nM')
    plt.plot(sim.t,sim.Akt_act[:,6]/18.8,':',label='EGF=10 nM')
    plt.title('EGF increasing HRG=0.5 nM')
    plt.xlim(0,1900)
    plt.xticks([0,500,1000,1500])
    plt.xlabel('Time (s)')
    plt.ylim(0,1.5)
    plt.yticks([0,0.5,1,1.5])
    plt.ylabel('Normalized Akt*')
    plt.legend(loc='upper right',fontsize=8)

    plt.subplot(4,2,6)
    plt.plot(sim.t,sim.Akt_act[:,1]/18.8,'-',label='EGF=0 nM')
    plt.plot(sim.t,sim.Akt_act[:,4]/18.8,'--',label='EGF=0.5 nM')
    plt.plot(sim.t,sim.Akt_act[:,7]/18.8,':',label='EGF=10 nM')
    plt.title('EGF increasing HRG=10 nM')
    plt.xlim(0,1900)
    plt.xticks([0,500,1000,1500])
    plt.xlabel('Time (s)')
    plt.ylim(0,1.5)
    plt.yticks([0,0.5,1,1.5])
    plt.ylabel('Normalized Akt*')
    plt.legend(loc='upper right',fontsize=8)

    plt.subplot(4,2,7)
    plt.plot(sim.t,sim.Akt_act[:,2]/18.8,'-',label='HRG=0 nM')
    plt.plot(sim.t,sim.Akt_act[:,3]/18.8,'--',label='HRG=0.5 nM')
    plt.plot(sim.t,sim.Akt_act[:,4]/18.8,':',label='HRG=10 nM')
    plt.title('EGF=0.5 nM HRG increasing')
    plt.xlim(0,1900)
    plt.xticks([0,500,1000,1500])
    plt.xlabel('Time (s)')
    plt.ylim(0,1.5)
    plt.yticks([0,0.5,1,1.5])
    plt.ylabel('Normalized Akt*')
    plt.legend(loc='upper right',fontsize=8)

    plt.subplot(4,2,8)
    plt.plot(sim.t,sim.Akt_act[:,5]/18.8,'-',label='HRG=0 nM')
    plt.plot(sim.t,sim.Akt_act[:,6]/18.8,'--',label='HRG=0.5 nM')
    plt.plot(sim.t,sim.Akt_act[:,7]/18.8,':',label='HRG=10 nM')
    plt.title('EGF=10 nM HRG increasing')
    plt.xlim(0,1900)
    plt.xticks([0,500,1000,1500])
    plt.xlabel('Time (s)')
    plt.ylim(0,1.5)
    plt.yticks([0,0.5,1,1.5])
    plt.ylabel('Normalized Akt*')
    plt.legend(loc='upper right',fontsize=8)

    plt.show()