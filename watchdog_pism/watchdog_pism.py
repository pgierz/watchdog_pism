"""Main module."""

import logging
import time

def set_up_logging(logfile):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename=logfile)

def check_for_max_sia_diffusivity(slurm_out):
    with open(slurm_out) as l:
        contents = l.read()
        if "PISM ERROR: Maximum diffusivity of SIA flow" in contents:
            try:
                with open("max_diffusivity_handled.dat", "r") as error_handle_file:
                    error_count = int(error_handle_file.read())
                    error_count += 1
            except IOError:
                error_count = 1
            with open("max_diffusivity_handled.dat", "w") as error_handle_file:
                error_handle_file.write(error_count)

            if error_count > 10:
                logging.info("Error count exceeded 10 times, letting model fail...")
            else:
                handle_max_diffusivity()

def handle_max_diffusivity():
    with open(RUNSCRIPT_FILE) as runscript:
        old_runscript = runscript.readlines()
    for indx, line in enumerate(old_runscript):
        if line.startswith("pism_set_config_value___stress_balance___sia___max_diffusivity"):
            key, value = line.split("=")
            save_index = indx
            value = float(value)
            value *= 1.1
            new_line = key+"="+str(value)
    old_runscript[save_index] = new_line
    with open(RUNSCRIPT_FILE, "w") as runscript:
        for line in old_runscript:
            runscript.write(line)
    # Cancel the job if it is still running:


if __name__ == "__main__":

    path = "/work/ollie/pgierz/PISM/pindex_vostok_ds50/scripts"
    path = "/work/ollie/pgierz/PISM/pindex_vostok_ds30/"
    #go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)

    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()
