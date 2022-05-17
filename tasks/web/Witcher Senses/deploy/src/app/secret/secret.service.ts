import { Injectable } from '@angular/core';
import { environment } from "../../environments/environment";
import CryptoJS from "crypto-js";

@Injectable({
  providedIn: 'root'
})
export class SecretService {

  constructor() { }

  getFlag(): string {
    return CryptoJS.AES.decrypt(environment.flag, environment.key).toString(CryptoJS.enc.Utf8);
  }
}
