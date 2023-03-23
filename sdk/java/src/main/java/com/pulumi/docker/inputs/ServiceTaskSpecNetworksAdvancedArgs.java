// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.docker.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class ServiceTaskSpecNetworksAdvancedArgs extends com.pulumi.resources.ResourceArgs {

    public static final ServiceTaskSpecNetworksAdvancedArgs Empty = new ServiceTaskSpecNetworksAdvancedArgs();

    @Import(name="aliases")
    private @Nullable Output<List<String>> aliases;

    public Optional<Output<List<String>>> aliases() {
        return Optional.ofNullable(this.aliases);
    }

    @Import(name="driverOpts")
    private @Nullable Output<List<String>> driverOpts;

    public Optional<Output<List<String>>> driverOpts() {
        return Optional.ofNullable(this.driverOpts);
    }

    /**
     * Name of the service
     * 
     */
    @Import(name="name", required=true)
    private Output<String> name;

    /**
     * @return Name of the service
     * 
     */
    public Output<String> name() {
        return this.name;
    }

    private ServiceTaskSpecNetworksAdvancedArgs() {}

    private ServiceTaskSpecNetworksAdvancedArgs(ServiceTaskSpecNetworksAdvancedArgs $) {
        this.aliases = $.aliases;
        this.driverOpts = $.driverOpts;
        this.name = $.name;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(ServiceTaskSpecNetworksAdvancedArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private ServiceTaskSpecNetworksAdvancedArgs $;

        public Builder() {
            $ = new ServiceTaskSpecNetworksAdvancedArgs();
        }

        public Builder(ServiceTaskSpecNetworksAdvancedArgs defaults) {
            $ = new ServiceTaskSpecNetworksAdvancedArgs(Objects.requireNonNull(defaults));
        }

        public Builder aliases(@Nullable Output<List<String>> aliases) {
            $.aliases = aliases;
            return this;
        }

        public Builder aliases(List<String> aliases) {
            return aliases(Output.of(aliases));
        }

        public Builder aliases(String... aliases) {
            return aliases(List.of(aliases));
        }

        public Builder driverOpts(@Nullable Output<List<String>> driverOpts) {
            $.driverOpts = driverOpts;
            return this;
        }

        public Builder driverOpts(List<String> driverOpts) {
            return driverOpts(Output.of(driverOpts));
        }

        public Builder driverOpts(String... driverOpts) {
            return driverOpts(List.of(driverOpts));
        }

        /**
         * @param name Name of the service
         * 
         * @return builder
         * 
         */
        public Builder name(Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name Name of the service
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        public ServiceTaskSpecNetworksAdvancedArgs build() {
            $.name = Objects.requireNonNull($.name, "expected parameter 'name' to be non-null");
            return $;
        }
    }

}
