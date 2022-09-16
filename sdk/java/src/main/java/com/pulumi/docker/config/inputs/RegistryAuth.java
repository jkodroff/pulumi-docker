// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.docker.config.inputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class RegistryAuth {
    private final String address;
    private final @Nullable String configFile;
    private final @Nullable String configFileContent;
    private final @Nullable String password;
    private final @Nullable String username;

    @CustomType.Constructor
    private RegistryAuth(
        @CustomType.Parameter("address") String address,
        @CustomType.Parameter("configFile") @Nullable String configFile,
        @CustomType.Parameter("configFileContent") @Nullable String configFileContent,
        @CustomType.Parameter("password") @Nullable String password,
        @CustomType.Parameter("username") @Nullable String username) {
        this.address = address;
        this.configFile = configFile;
        this.configFileContent = configFileContent;
        this.password = password;
        this.username = username;
    }

    public String address() {
        return this.address;
    }
    public Optional<String> configFile() {
        return Optional.ofNullable(this.configFile);
    }
    public Optional<String> configFileContent() {
        return Optional.ofNullable(this.configFileContent);
    }
    public Optional<String> password() {
        return Optional.ofNullable(this.password);
    }
    public Optional<String> username() {
        return Optional.ofNullable(this.username);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(RegistryAuth defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private String address;
        private @Nullable String configFile;
        private @Nullable String configFileContent;
        private @Nullable String password;
        private @Nullable String username;

        public Builder() {
    	      // Empty
        }

        public Builder(RegistryAuth defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.address = defaults.address;
    	      this.configFile = defaults.configFile;
    	      this.configFileContent = defaults.configFileContent;
    	      this.password = defaults.password;
    	      this.username = defaults.username;
        }

        public Builder address(String address) {
            this.address = Objects.requireNonNull(address);
            return this;
        }
        public Builder configFile(@Nullable String configFile) {
            this.configFile = configFile;
            return this;
        }
        public Builder configFileContent(@Nullable String configFileContent) {
            this.configFileContent = configFileContent;
            return this;
        }
        public Builder password(@Nullable String password) {
            this.password = password;
            return this;
        }
        public Builder username(@Nullable String username) {
            this.username = username;
            return this;
        }        public RegistryAuth build() {
            return new RegistryAuth(address, configFile, configFileContent, password, username);
        }
    }
}