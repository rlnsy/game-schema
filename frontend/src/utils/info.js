import axios from 'axios'
import { infoBaseUrl } from './constants'

export async function getInfo() {
    return await axios({
        method: 'get',
        url: infoBaseUrl,
        params: {
            body: {}
        }
    }).catch((e) => {
      throw e;
    });
}
