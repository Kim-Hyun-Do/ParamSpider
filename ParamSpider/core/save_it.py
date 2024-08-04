import os
import errno


def save_func(final_urls, outfile):
    if "/" in outfile:
        filename = outfile
    else:
        filename = f'output/{outfile}'

    print(f"Saving to file: {filename}")


    if os.path.exists(filename):
        os.remove(filename)


    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise


    if not final_urls:
        print("The final_urls list is empty. Nothing to write.")
        return


    try:
        with open(filename, "a", encoding="utf-8") as f:
            for i in final_urls:
                f.write(i + "\n")
        print(f"Successfully written to {filename}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")